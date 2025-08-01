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
    document.getElementById('new-place-form').onsubmit = function(event) {
    event.preventDefault();
    const name = document.getElementById('place-name').value;
    fetch('http://localhost:5001/api/v1/amenities/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name })
    })
    .then(response => {
        if (response.ok) {
            // Ajoute l'amenity dans la liste amenities
            const ul = document.querySelector('#amenities ul.row');
            const li = document.createElement('li');
            li.innerHTML = `
                <div class="amenity-widget" style="border:1px solid #ccc; border-radius:8px; padding:1rem; margin:1rem 0; background:#fafafa;">
                    <strong>${name}</strong><br>
                    <button class="louer-btn" style="margin:0.5rem;">Louer</button>
                    <button class="visiter-btn" style="margin:0.5rem;">Visiter</button>
                </div>
            `;
            ul.appendChild(li);

            li.querySelector('.louer-btn').onclick = function() {
                alert('Fonction Louer à implémenter');
            };
            li.querySelector('.visiter-btn').onclick = function() {
                alert('Fonction Visiter à implémenter');
            };

            alert('Amenity créée avec succès !');
            document.getElementById('place-popup').style.display = 'none';
        } else {
            alert('Erreur lors de la création de l\'amenity.');
        }
    });
};
    .then(response => {
    if (response.ok) {
        const ul = document.querySelector('#places ul.row');
        const li = document.createElement('li');
        li.innerHTML = `
            <div class="place-widget" style="border:1px solid #ccc; border-radius:8px; padding:1rem; margin:1rem 0; background:#fafafa;">
                <strong>${name}</strong><br>
                Chambres: ${rooms} | Surface: ${surface} m² | Capacité: ${capacity} personnes<br>
                <button class="louer-btn" style="margin:0.5rem;">Louer</button>
                <button class="visiter-btn" style="margin:0.5rem;">Visiter</button>
            </div>
        `;
        ul.appendChild(li);

        // Actions pour les boutons (exemple)
        li.querySelector('.louer-btn').onclick = function() {
            alert('Fonction Louer à implémenter');
        };
        li.querySelector('.visiter-btn').onclick = function() {
            alert('Fonction Visiter à implémenter');
        };

        alert('Place créée avec succès !');
        document.getElementById('place-popup').style.display = 'none';
    } else {
        alert('Erreur lors de la création de la place.');
    }
});
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
