from abc import ABC, abstractmethod
from app.persistence.repository import Repository
from app import db


class Repository(ABC):
    @abstractmethod
    def add(self, obj):
        pass

    @abstractmethod
    def get(self, obj_id):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def update(self, obj_id, data):
        pass

    @abstractmethod
    def delete(self, obj_id):
        pass

    @abstractmethod
    def get_by_attribute(self, attr_name, attr_value):
        pass


class InMemoryRepository(Repository):
    def __init__(self):
        self._storage = {}

    def add(self, obj):
        self._storage[obj.id] = obj

    def get(self, obj_id):
        try:
            obj_id = uuid.UUID(str(obj_id))
        except ValueError:
            return None
        return self._storage.get(obj_id)

    def get_all(self):
        return list(self._storage.values())

    def update(self, obj_id, data):
        obj = self.get(obj_id)
        if obj:
            obj.update(data)
            return obj
        return None

    def delete(self, obj_id):
        try:
            obj_id = uuid.UUID(str(obj_id))
        except ValueError:
            return False
        return self._storage.pop(obj_id, None) is not None

    def get_by_attribute(self, attr_name, attr_value):
        return next((obj for obj in self._storage.values() if getattr(obj, attr_name) == attr_value), None)

class SQLAlchemyRepository(Repository):
    def __init__(self, model):
        self.model = model  # Le modèle SQLAlchemy à gérer

    def add(self, obj):
        """Ajoute un nouvel objet dans la base"""
        db.session.add(obj)
        db.session.commit()

    def get(self, obj_id):
        """Récupère un objet par son ID"""
        return self.model.query.get(obj_id)

    def get_all(self):
        """Retourne tous les objets"""
        return self.model.query.all()

    def update(self, obj_id, data):
        """Met à jour un objet existant"""
        obj = self.get(obj_id)
        if obj:
            for key, value in data.items():
                setattr(obj, key, value)  # Mise à jour dynamique des attributs
            db.session.commit()

    def delete(self, obj_id):
        """Supprime un objet"""
        obj = self.get(obj_id)
        if obj:
            db.session.delete(obj)
            db.session.commit()

    def get_by_attribute(self, attr_name, attr_value):
        """Recherche un objet via un attribut dynamique"""
        return self.model.query.filter_by(**{attr_name: attr_value}).first()
    