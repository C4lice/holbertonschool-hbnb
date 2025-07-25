# HBnB - Testing Process Documentation

## :clipboard: Overview
This document provides a comprehensive overview of the testing process conducted for the HBnB RESTful API project. The testing strategy includes both manual and automated approaches:<br>

Manual Testing: Performed using cURL commands to interact with the API endpoints directly, validating their input/output formats, HTTP status codes, and validation rules.<br>

Automated Testing: Implemented using Python's unittest module to ensure endpoint correctness, data validation, and consistent behavior under various scenarios including edge cases and erroneous input.<br>

The entities tested include Users, Places, Amenities, and Reviews. Each endpoint was verified for creation, retrieval (single and all), validation errors, and updates where applicable.<br>

## 1.Testing the Endpoints Using cURL

### :pencil2: Testing case for Users (Example)

**case1. Creation of a user**
```
curl -X POST "http://127.0.0.1:5000/api/v1/users/" -H "Content-Type: application/json" -d '{
    "first_name": "Jane",
    "last_name": "Doe",
    "email": "jane.doe@example.com"
}
```
Expected Response:
```
{
    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "first_name": "Jane",
    "last_name": "Doe",
    "email": "jane.doe@example.com"
}
```
// 201 Created<br>

**Case2. Creation user with invalide data**
```
 curl -X POST "http://127.0.0.1:5000/api/v1/users/" -H "Content-Type: application/json" -d '{
    "first_name": "",
    "last_name": "Doe",
    "email": "invalid-email"
}
```
Expected Response:
```
{
    "error": "First name cannot be empty."
}
```
// 400 Bad Request<br>

**case3. Retrieve non-existent user**
```
curl -X GET  "http://127.0.0.1:5000/api/v1/users/nonexixtent_id" 
```
Expected Response:
```
{
    "error": "User not found"
}
```
//404 Not found<br>


## 2. Swagger Documentation
**🔹 Accessing Swagger UI<br>**
Swagger UI is automatically generated by Flask-RESTx and can be accessed by navigating to the following URL while the development server is running:
```
http://127.0.0.1:5000/api/v1/
```
This interface provides:<br>

・A list of all available endpoints grouped by resource (e.g., /users/,
   /places/, etc.)<br>
・The request and response format for each endpoint<br>
・Try-it-out functionality to test endpoints directly from the   
   browser<br>
・ Auto-validation based on defined @api.expect models<br>
**🔹 Model Definitions<br>**
Each model is described using @api.model, and these definitions are reflected in the Swagger UI. <br>
For example:<br>
User Model Example:<br>
```
user_model = api.model('User', {
    'first_name': fields.String(required=True, description='The user\'s first name'),
    'last_name': fields.String(required=True, description='The user\'s last name'),
    'email': fields.String(required=True, description='The user\'s email')
})
```
In Swagger, this appears under Definitions and is used to validate request bodies for POST/PUT.<br>
**🔹 Swagger Testing Example<br>**
For manual testing, the Swagger UI was used to verify:<br>

✅ Correct request payload structure<br>

✅ Automatic validation of required fields<br>

✅ Error responses for invalid inputs<br>

✅ Successful creation and retrieval of resources<br><br>
**Example:**<br>
Endpoint: POST /api/v1/users/<br>
Input: Valid JSON body with all required fields<br><br>
**Swagger Result:**<br>

 ・HTTP 201 Created<br>
 ・Response body matches expected schema<br>
![Image](https://github.com/user-attachments/assets/d864addb-68c5-4958-b722-b53e5ad2d215)<br>
**:small_blue_diamond:Summary**<br>
 
・Swagger UI played a crucial role in black-box and manual testing.<br>
・It helped confirm that:<br>

-All endpoints are documented and accessible.<br>
-Models are correctly defined and validated.<br>
-Error handling works as expected before hitting the backend.<br>

・It complements unit tests and cURL by offering real-time, visual API
   verification.

## 3.Unit Tests
**:large_orange_diamond:Unit  Test Users(Example)<br>**
```
import unittest
from app import create_app

class TestUserEndpoints(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_create_user(self):
        response = self.client.post('/api/v1/users/', json={
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "jane.doe@example.com"
        })
        self.assertEqual(response.status_code, 201)

    def test_create_user_invalid_data(self):
        response = self.client.post('/api/v1/users/', json={
            "first_name": "",
            "last_name": "Doe",
            "email": "invalid-email"
        })
        self.assertEqual(response.status_code, 400)

    def test_get_non_existent_user(self):
        response = self.client.get('/api/v1/users/nonexixtent_id')
        self.assertEqual(response.status_code, 404)

    def test_get_all_users(self):
        response = self.client.get('api/v1/users/')
        self.assertEqual(response.status_code, 200)
        users = response.get_json()
        self.assertIsInstance(users, list)
        self.assertGreaterEqual(len(users), 1)
    
    def test_put_user_update(self):
        create_response = self.client.post('/api/v1/users/', json={
            "first_name": ":Michel",
            "last_name": "Smith",
            "email": "michel.smith@example.com"
        })
        self.assertEqual(create_response.status_code, 201)
        user = create_response.get_json()
        user_id = user['id']
        update_data = {
            "first_name": "Mary",
            "last_name": "Smith",
            "email": "mary.smith@example.com"
        }
        update_response = self.client.put(f'/api/v1/users/{user_id}', json=update_data)
        self.assertEqual(update_response.status_code, 200)
        updated_user = update_response.get_json()
        self.assertEqual(updated_user['first_name'], "Mary")
        self.assertEqual(updated_user['email'], "mary.smith@example.com")


if __name__ == '__main__':
    unittest.main()
```
**:arrow_right: Result**
```
python -m unittest -v tests.test_users
test_create_user (tests.test_users.TestUserEndpoints.test_create_user) ... ok
test_create_user_invalid_data (tests.test_users.TestUserEndpoints.test_create_user_invalid_data) ... ok
test_get_all_users (tests.test_users.TestUserEndpoints.test_get_all_users) ... ok
test_get_non_existent_user (tests.test_users.TestUserEndpoints.test_get_non_existent_user) ... ok
test_put_user_update (tests.test_users.TestUserEndpoints.test_put_user_update) ... ok
----------------------------------------------------------------------
Ran 5 tests in 0.021s

OK
```

## :pushpin:Conclusion<br>
 The testing process demonstrated that:<br>

All main API endpoints respond correctly under normal and erroneous conditions.<br>

Validation logic is enforced properly, with meaningful error messages and accurate HTTP status codes.<br>

The system is resilient against bad input and correctly handles non-existent resources.<br>

Both manual (via cURL) and automated (via unit tests) methods confirm the robustness and correctness of the API.<br>

As a result, the HBnB API shows strong compliance with expected behavior and is ready for integration with a frontend or further deployment.<br>

