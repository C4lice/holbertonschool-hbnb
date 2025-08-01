from flask import request
from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from app.services import facade
from app.models.user import User
from app.api.v1.amenities import amenity_model

admin_api = Namespace('admin', description='Admin operations')


@admin_api.route('/bootstrap/admin/')
class BootstrapAdmin(Resource):
    def post(self):
        """
        Create an initial admin user.
        ⚠️ Use only once! Delete this route after bootstrapping.
        """
        user_data = request.json
        if not user_data.get('email') or not user_data.get('password'):
            return {'error': 'Email and password are required.'}, 400

        if facade.get_user_by_email(user_data['email']):
            return {'error': 'Email already registered'}, 400

        try:
            new_admin = facade.create_user(user_data, force_admin=True)
        except Exception as e:
            return {'error': str(e)}, 400

        return {
            'id': str(new_admin.id),
            'first_name': new_admin.first_name,
            'last_name': new_admin.last_name,
            'email': new_admin.email,
            'is_admin': new_admin.is_admin
        }, 201


@admin_api.route('/users/<user_id>')
class AdminUserResource(Resource):
    @jwt_required()
    def put(self, user_id):
        claims = get_jwt()
        if not claims.get('is_admin'):
             return {'error': 'Admin privileges required'}, 403

        data = request.json

        if 'email' in data:
            existing_user = facade.get_user_by_email(data['email'])
            if existing_user and str(existing_user.id) != user_id:
                return {'error': 'Email already in use'}, 400

        updated_user = facade.update_user(user_id, data)
        if not updated_user:
            return {'error': 'User not found'}, 404

        return {
            'id': str(updated_user.id),
            'first_name': updated_user.first_name,
            'last_name': updated_user.last_name,
            'email': updated_user.email,
            'is_admin': updated_user.is_admin
        }, 200



    @jwt_required()
    def delete(self, user_id):
        claims = get_jwt()
        if not claims.get('is_admin'):
            return {'error': 'Admin privileges required'}, 403

        deleted = facade.user_repo.delete(user_id)
        if not deleted:
            return {'error': 'User not found'}, 404

        return {'message': 'User deleted'}, 204


@admin_api.route('/amenities')
class AdminAmenityCreate(Resource):
     @admin_api.expect(amenity_model, validate=True)
     @admin_api.response(201, 'Amenity successfully created')
     @jwt_required()
     def post(self):
        claims = get_jwt()
        if not claims.get('is_admin'):
            return {'error': 'Admin privileges required'}, 403
         
        amenity_data = request.json

        try:
            new_amenity = facade.create_amenity(amenity_data)
        except ValueError as e:
            return {'error': str(e)}, 400

        return {
             'id': str(new_amenity.id),
             'name': new_amenity.name
         }, 201


@admin_api.route('/amenities/<amenity_id>')
class AdminAmenityModify(Resource):
    @admin_api.expect(amenity_model, validate=True)
    @admin_api.response(200, 'Amenity successfully updated')
    @admin_api.response(404, 'Amenity not found')
    @jwt_required()
    def put(self, amenity_id):
        claims = get_jwt()
        if not claims.get('is_admin'):
            return {'error': 'Admin privileges required'}, 403
    
        amenity_data = request.json
    
        updated_amenity = facade.update_amenity(amenity_id, amenity_data)
        if not updated_amenity:
            return {'error': 'Amenity not found'}, 404
        
        return {
            'id': str(updated_amenity.id),
            'name': updated_amenity.name
        }, 200
    
    @jwt_required()
    def delete(self, amenity_id):
        claims = get_jwt()
        if not claims.get('is_admin'):
            return {'error': 'Admin privileges required'}, 403

        deleted = facade.delete_amenity(amenity_id)
        if not deleted:
            return {'error': 'Amenity not found'}, 404

        return {'message': 'Amenity deleted'}, 204