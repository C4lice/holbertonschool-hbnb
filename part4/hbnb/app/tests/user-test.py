import unittest
from app import create_app

class TestUserEndpoints(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def _create_user(self, first_name="Jane", last_name="Doe", email="jane.doe@example.com", password="toto"):
        response = self.client.post('/api/v1/users/', json={
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "password": password
        })
        return response

    def _login_user(self, email, password):
        response = self.client.post('/api/v1/auth/login', json={
            "email": email,
            "password": password
        })
        return response.get_json()["access_token"]

    # --- Création d'utilisateur ---
    def test_create_user_success(self):
        response = self._create_user()
        self.assertEqual(response.status_code, 201)

    def test_create_user_invalid_email(self):
        response = self._create_user(email="invalid-email")
        self.assertEqual(response.status_code, 400)

    def test_create_user_invalid_first_name(self):
        response = self._create_user(first_name="x" * 300)
        self.assertEqual(response.status_code, 400)

    def test_create_user_invalid_last_name(self):
        response = self._create_user(last_name="x" * 300)
        self.assertEqual(response.status_code, 400)

    def test_create_user_empty_fields(self):
        response = self._create_user(first_name="", last_name="", email="invalid", password="toto")
        self.assertEqual(response.status_code, 400)

    # --- Data recovery ---
    def test_get_user_by_id(self):
        user = self._create_user(email="jane1@example.com")
        user_id = user.get_json()["id"]
        response = self.client.get(f'/api/v1/users/{user_id}')
        self.assertEqual(response.status_code, 200)

    def test_get_user_by_invalid_id(self):
        response = self.client.get('/api/v1/users/invalidid123')
        self.assertEqual(response.status_code, 404)

    def test_get_all_users(self):
        response = self.client.get('/api/v1/users/')
        self.assertEqual(response.status_code, 200)

    # --- User update ---
    def test_update_user_success(self):
        user_resp = self._create_user(email="update1@example.com")
        user = user_resp.get_json()
        token = self._login_user("update1@example.com", "toto")

        response = self.client.put(
            f'/api/v1/users/{user["id"]}',
            headers={'Authorization': f'Bearer {token}'},
            json={"first_name": "Updated", "last_name": "Name"}
        )
        self.assertEqual(response.status_code, 200)

    def test_update_user_invalid_fields(self):
        user_resp = self._create_user(email="update2@example.com")
        user = user_resp.get_json()
        token = self._login_user("update2@example.com", "toto")

        response = self.client.put(
            f'/api/v1/users/{user["id"]}',
            headers={'Authorization': f'Bearer {token}'},
            json={"first_name": "", "last_name": "Doe", "email": "notanemail"}
        )
        self.assertEqual(response.status_code, 400)

    def test_update_user_too_long_names(self):
        user_resp = self._create_user(email="longname@example.com")
        user = user_resp.get_json()
        token = self._login_user("longname@example.com", "toto")

        response = self.client.put(
            f'/api/v1/users/{user["id"]}',
            headers={'Authorization': f'Bearer {token}'},
            json={"first_name": "x" * 300, "last_name": "x" * 300}
        )
        self.assertEqual(response.status_code, 400)

    def test_update_user_not_found(self):
        user_resp = self._create_user(email="notfound@example.com")
        token = self._login_user("notfound@example.com", "toto")

        response = self.client.put(
            '/api/v1/users/nonexistentid',
            headers={'Authorization': f'Bearer {token}'},
            json={"first_name": "Ghost", "last_name": "User"}
        )
        self.assertEqual(response.status_code, 404)

    # --- Sécurité / JWT ---
    def test_update_user_with_wrong_token(self):
        u1 = self._create_user(email="j1@example.com")
        u1_id = u1.get_json()["id"]
        self._create_user(email="j2@example.com")
        token = self._login_user("j2@example.com", "toto")

        # Attempt to update the user of another account
        response = self.client.put(
            f'/api/v1/users/{u1_id}',
            headers={'Authorization': f'Bearer {token}'},
            json={"first_name": "Hack"}
        )
        self.assertEqual(response.status_code, 403)

    def test_update_user_with_invalid_fields(self):
        u = self._create_user(email="j3@example.com")
        user = u.get_json()
        token = self._login_user("j3@example.com", "toto")

        # Champ non modifiable : password
        response = self.client.put(
            f'/api/v1/users/{user["id"]}',
            headers={'Authorization': f'Bearer {token}'},
            json={"password": "newpass"}
        )
        self.assertEqual(response.status_code, 400)

        # Email update interdit
        response = self.client.put(
            f'/api/v1/users/{user["id"]}',
            headers={'Authorization': f'Bearer {token}'},
            json={"email": "hack@ex.com"}
        )
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()
