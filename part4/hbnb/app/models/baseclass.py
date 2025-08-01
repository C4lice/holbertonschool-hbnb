import uuid
from datetime import datetime, timezone
from app import db

class BaseModel(db.model):
    __abstract__ = True
  
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    def save(self):
        """Save the current state of the object to the database."""
        self.updated_at = datetime.now()

    def update(self, data):
        """Update the object's attributes with the provided data."""
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.save()

    @abstractmethod
    def to_dict(self):
        pass
