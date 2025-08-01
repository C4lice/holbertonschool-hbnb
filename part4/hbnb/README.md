# HBnB- Enhanced Backend with Authentication and Database Integration

## Overview
This part of the project builds on the RESTful foundation of the HBnB platform by adding important production-ready features. It sets up a persistent SQL database with SQLAlchemy, implements secure JWT-based authentication with hashed passwords, and defines clear relational models for users, places, reviews, and amenities. Together, these additions make the backend more robust, maintainable, and secure — bringing it in line with modern standards for professional web applications.

### ✏️ The Project Directory Structure:
```
hbnb/
├── app/
│   ├── __init__.py
|   ├── extensions.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── v1/
│   │       ├── __init__.py
│   │       ├── users.py
│   │       ├── places.py
│   │       ├── reviews.py
│   │       ├── amenities.py
|   |       ├── admin.py
|   |       ├── auth.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── place.py
│   │   ├── review.py
│   │   ├── amenity.py
|   |   ├── baseclass.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── facade.py
│   ├── persistence/
│       ├── __init__.py
│       ├── repository.py
├── run.py
├── config.py
├── requirements.txt
├── README.md
```
## :bulb:Installation & Run the application

 1. Clone the repository:<br>
 ``` 
    https://github.com/C4lice/holbertonschool-hbnb.git 
 ``` 

 2. Create a Virtual Environment (Recommended) <br>
```  
python3 -m venv venv  
source venv/bin/activate  
``` 
 3. Install Dependencies<br>
  ```
pip install -r requirements.txt
```
4.Run the application<br>
```
 python run.py
 ```

## :key: Environment Requirements

 - Python 3.8+<br>
 - pip (Python package manager)<br>

## 🧩 Technologies

- **Flask**
- **SQLAlchemy**
- **Flask-JWT-Extended**
- **Flask-Bcrypt**

## 🔑 Authentication

- Register with `/api/v1/users/`
- Login with `/api/v1/auth/login` to get a JWT
- Add `Authorization: Bearer <token>` to protected requests

## 🗃️ Database

- SQLite for local dev
- MySQL ready for production
- Models: User, Place, Review, Amenity
- Relationships: User → Place → Review, Place ↔ Amenity

 
## Authors
[Laura Aupetit](https://github.com/C4lice)<br>
[Emi Hatano](https://github.com/Emi-H106)

