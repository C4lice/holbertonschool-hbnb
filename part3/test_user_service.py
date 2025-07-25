from app import create_app
from app.extensions import db
from app.services.facade import UserService

app = create_app()
app.app_context().push()

# Nettoyage de la base
db.drop_all()
db.create_all()

# Initialisation du service
service = UserService()

# ✅ Créer un utilisateur
print("\nCréation utilisateur...")
user = service.create_user({
    "first_name": "John",
    "last_name": "Doe",
    "email": "john@example.com",
    "password": "supersecret",
    "is_admin": True
})
print("Utilisateur créé :", user)

# ✅ Récupérer tous les utilisateurs
print("\nListe des utilisateurs :")
for u in service.get_all():
    print(u)

# ✅ Vérifier le mot de passe (authentification)
print("\nAuthentification avec le bon mot de passe :")
auth_user = service.authenticate("john@example.com", "supersecret")
print("Résultat :", auth_user)

print("\nAuthentification avec un mauvais mot de passe :")
bad_auth = service.authenticate("john@example.com", "wrongpassword")
print("Résultat :", bad_auth)

# ✅ Mise à jour utilisateur
print("\nMise à jour de l'utilisateur :")
updated_user = service.update(user.id, {"first_name": "Johnny"})
print("Utilisateur mis à jour :", updated_user)

# ✅ Suppression utilisateur
print("\nSuppression de l'utilisateur :")
deleted = service.delete(user.id)
print("Supprimé :", deleted)
