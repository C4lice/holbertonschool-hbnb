from app import db
from app.models.base_model import BaseModel
from sqlalchemy.orm import validates

class Review(BaseModel):
    __tablename__ = 'review'

    text = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.String(36), db.ForeignKey('user.id'), nullable=False)
    place_id = db.Column(db.String(36), db.ForeignKey('place.id'), nullable=False)

    # constraint: a user can rate a location only once
    __table_args__ = (
        db.UniqueConstraint('user_id', 'place_id', name='uq_user_place_review'),
    )

    # validation: rating must be between 1 and 5
    @validates("rating")
    def validate_rating(self, key, rating):
        if 1 <= rating <= 5:
            return rating
        raise ValueError("Rating must be between 1 and 5")

    # validation: text must not be empty
    @validates("text")
    def validate_text(self, key, text):
        if text and text.strip():
            return text
        raise ValueError("The review text must not be empty")

    # setting up a JSON response
    def to_dict(self):
        return {

            'id': self.id,
            'place': self.place_id,
            'user': self.user_id,
            'rating': self.rating,
            'text': self.text
        }
