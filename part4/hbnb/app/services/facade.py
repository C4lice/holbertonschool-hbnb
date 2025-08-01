from app.persistence.repository import InMemoryRepository
from app.models.user import User
from app.models.place import Place
from app.models.amenity import Amenity
from app.models.review import Review
from app.models.user import User
from app.persistence.repository import SQLAlchemyRepository

from app.models.user import User
from app.models.place import Place
from app.models.amenity import Amenity
from app.models.review import Review
from app.persistence.repository import InMemoryRepository

class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    def create_user(self, user_data):
        user = User(**user_data)
        user.hash_password(user_data['password'])
        self.user_repo.add(user)
        return user
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        return self.user_repo.get(user_id)

    def get_all_user(self):
        return self.user_repo.get_all()

    def get_user_by_email(self, email):
        return self.user_repo.get_by_attribute('email', email)

    def update_user(self, user_id, user_data):
        user = self.get_user(user_id)
        if user:
            user.update(user_data)
            self.user_repo.update(user_id, user_data)
        return user
    
    def delete_user(self, user_id):
        return self.user_repo.delete(user_id)

    def create_place(self, place_data):
        place = Place(**place_data)
        self.place_repo.add(place)
        return place

    def get_place(self, place_id):
        return self.place_repo.get(place_id)

    def get_all_places(self):
        return self.place_repo.get_all()

    def update_place(self, place_id, place_data):
        place = self.get_place(place_id)
        if place:
            place.update(place_data)
            self.place_repo.update(place_id, place_data)
        return place
    
    def delete_place(self, place_id):
        return self.place_repo.delete(place_id)

    def create_amenity(self, amenity_data):
        amenity = Amenity(**amenity_data)
        self.amenity_repo.add(amenity)
        return amenity

    def get_amenity(self, amenity_id):
        return self.amenity_repo.get(amenity_id)

    def get_all_amenities(self):
        return self.amenity_repo.get_all()

    def update_amenity(self, amenity_id, amenity_data):
        amenity = self.get_amenity(amenity_id)
        if amenity:
            amenity.update(amenity_data)
            self.amenity_repo.update(amenity_id, amenity_data)
        return amenity
    
    def delete_amenity(self, amenity_id):
        return self.amenity_repo.delete(amenity_id)

    # --- PLACES ---
    def create_place(self, place_data):
        owner = self.get_user(place_data.pop("owner_id"))
        amenities = [self.get_amenity(a_id) for a_id in place_data.pop("amenities", [])]

        place_data["owner"] = owner
        place_data["amenities"] = amenities

        place = Place(**place_data)
        self.place_repo.add(place)
        return place

    def get_place(self, place_id):
        return self.place_repo.get(place_id)

    def get_all_places(self):
        return self.place_repo.get_all()

    def update_place(self, place_id, place_data):
        place = self.get_place(place_id)
        if place:
            place.update(place_data)
            self.place_repo.update(place_id, place_data)
        return place

    # --- REVIEWS ---
    def create_review(self, review_data):
        # Validation des champs obligatoires
        required_fields = ['user_id', 'place_id', 'text']
        if not all(field in review_data for field in required_fields):
            raise ValueError("The fields user_id, place_id, and text are required")

        rating = review_data.get('rating')
        if rating is not None:
            if not isinstance(rating, int) or not (1 <= rating <= 5):
                raise ValueError("Rating must be an integer between 1 and 5")

        review_data['user'] = self.get_user(review_data.pop("user_id"))
        review_data['place'] = self.get_place(review_data.pop("place_id"))

        review = Review(**review_data)
        self.review_repo.add(review)
        return review

    def get_review(self, review_id):
        return self.review_repo.get(review_id)

    def get_all_reviews(self):
        return self.review_repo.get_all()

    def get_reviews_by_place(self, place_id):
        return self.review_repo.get_by_attribute('place_id', place_id)

    def update_review(self, review_id, review_data):
        review = self.get_review(review_id)
        if review:
            review.update(review_data)
            self.review_repo.update(review_id, review_data)
        return review

    def delete_review(self, review_id):
        return self.review_repo.delete(review_id)

    def get_reviews_by_place(self, place_id):
        return self.review_repo.get_by_attribute('place_id', place_id) or []
