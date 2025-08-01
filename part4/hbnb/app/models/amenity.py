from app.models.base_model import BaseModel
from app import db
from sqlalchemy.orm import validates

class Amenity(BaseModel):
    __tablename__ = 'amenities'

    name = db.Column(db.String(50), nullable=False)

    def __init__(self, name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name

    @validates("name")
    def validate_name(self, key, name):
        if name and len(name) <= 50:
            return name
        raise ValueError("Amenity name must not be empty and must be at most 50 characters long")

    def to_dict(self):
        return {

            "id": self.id,
            "name": self.name,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }
