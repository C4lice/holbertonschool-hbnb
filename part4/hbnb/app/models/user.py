from app.models.base_model import BaseModel
from app import db
from sqlalchemy.orm import validates
import re
from app.extensions import bcrypt

class User(BaseModel):

    __tablename__ = 'user'

    email = db.Column(db.String(120), nullable=False, unique=True)
    first_name = db.Column(db.String(60), nullable=False)
    last_name = db.Column(db.String(60), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    def __init__(self, email, first_name, last_name, password=None, is_admin=False, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.is_admin = is_admin
        if password:
            self.hash_password(password)
    
    def update(self, data):
        """Update user attributes with the provided data."""
        if 'first_name' in data:
            self.first_name = data['first_name']
        if 'last_name' in data:
            self.last_name = data['last_name']
        if 'email' in data:
            self.email = data['email']
        if 'password' in data:
            self.hash_password(data['password'])
        if 'is_admin' in data:
            self.is_admin = data['is_admin']

    @validates("email")
    def validate_email(self, key, value):
        if not value:
            raise ValueError("Email cannot be empty.")
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_regex, value):
            raise ValueError("Invalid email format.")
        return value

    @validates("first_name")
    def validate_first_name(self, key, value):
        if not value or not value.strip():
            raise ValueError("First name cannot be empty.")
        return value.strip()

    @validates("last_name")
    def validate_last_name(self, key, value):
        if not value or not value.strip():
            raise ValueError("Last name cannot be empty.")
        return value.strip()

    def hash_password(self, password):
        """Hashes the password before storing it."""
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def verify_password(self, password):
        """Verifies if the provided password matches the hashed password."""
        return bcrypt.check_password_hash(self.password, password)

    def update(self, data):
        """Update user attributes with the provided data."""
        if 'first_name' in data:
            self.first_name = data['first_name']
        if 'last_name' in data:
            self.last_name = data['last_name']
        if 'email' in data:
            self.email = data['email']
        if 'password' in data:
            self.hash_password(data['password'])
        if 'is_admin' in data:
            self.is_admin = data['is_admin']

    def to_dict(self):
        """Convert the user object to a dictionary."""
        return {
          
            'id': str(self.id),
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'is_admin': self.is_admin

        }
