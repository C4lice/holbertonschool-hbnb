from app.models.base_model import BaseModel
from app import db
from sqlalchemy.orm import relationship, validates

# Association table many-to-many
place_amenity = db.Table('place_amenity',
    db.Column('place_id', db.String(36), db.ForeignKey('place.id'), primary_key=True),
    db.Column('amenity_id', db.String(36), db.ForeignKey('amenities.id'), primary_key=True)
)

class Place(BaseModel):
    __tablename__ = 'places'

    id = Column(Integer, primary_key=True)
    owner_id = Column(Integer, nullable=False)
    title = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    city = Column(String(128), nullable=False)
    price = Column(Float, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    reviews = relationship('Review', backref='place', lazy=True)
    amenities = relationship('Amenity', secondary=place_amenity, backref=db.backref('places', lazy='dynamic'))

    @validates('title')
    def validate_title(self, key, value):
        if value == "" or len(value) > 50:
            raise ValueError("Title cannot be empty and must be less than 100 characters.")
        return value

    @validates('price')
    def validate_price(self, key, value):
        if value < 0:
            raise ValueError("Price must be a non-negative float.")
        return value

    @validates('latitude')
    def validate_latitude(self, key, value):
        if value is not None and not -90 <= value <= 90:
            raise ValueError("Latitude must be between -90 and 90.")
        return value

    @validates('longitude')
    def validate_longitude(self, key, value):
        if value is not None and not -180 <= value <= 180:
            raise ValueError("Longitude must be between -180 and 180.")
        return value

    def to_dict(self):
        """Convert the place object to a dictionary."""

        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "price": self.price,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "owner": self.owner.to_dict(),
            "amenities": [element.to_dict() for element in self.amenities],
            "reviews": [element.to_dict() for element in self.reviews]
        }
