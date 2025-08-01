from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from app.services import facade
from flask import request
from uuid import UUID

api = Namespace("reviews", description="Gestion des avis")

review_model = api.model("Review", {
    "id": fields.String(readonly=True),
    "user_id": fields.String(required=True),
    "place_id": fields.String(required=True),
    "rating": fields.Integer(required=True),
    "text": fields.String(required=True)
})

@api.route("/")
class ReviewListResource(Resource):
    @api.marshal_list_with(review_model)
    def get(self):
        """List all reviews"""
        return ｆacade.get_all_reviews()

    @api.expect(review_model, validate=True)
    @api.marshal_with(review_model, code=201)
    @jwt_required()
    def post(self):
        """Create a new notice"""
        current_user_id = get_jwt_identity()
        review_data = api.payload
        review_data['user_id'] = current_user_id

        place_id = review_data.get('place_id')
        if not place_id:
            api.abort(400, "place_id is required")
        place = facade.get_place(place_id)
        if not place:
            api.abort(404, "Place not found")
        if place.owner_id == current_user_id:
            api.abort(400, "You cannot review your own place.")
        existing_reviews = facade.get_reviews_by_place(place_id)
        for review in existing_reviews:
            if review.user_id == current_user_id:
                api.abort(400, "You have already reviewed this place.")
        try:
            return facade.create_review(api.payload), 201
        except ValueError as e:
            api.abort(400, str(e))

@api.route("/<string:review_id>")
@api.param("review_id", "Identifiant de l'avis")
class ReviewResource(Resource):
    @api.marshal_with(review_model)
    def get(self, review_id):
        """Recover a notice by ID"""
        review = facade.get_review(review_id)
        if not review:
            api.abort(404, "Avis non trouvé")
        return review

    @api.expect(review_model)
    @api.marshal_with(review_model)
    @jwt_required()
    def put(self, review_id):
        """Update a notice"""
        current_user_id = get_jwt_identity()
        claims = get_jwt()
        is_admin = claims.get('is_admin', False)

        if isinstance(current_user_id, dict):
            user_id = UUID(current_user_id.get('id'))
        else:
            user_id = UUID(current_user_id)

        review = facade.get_review(review_id)
        if not review:
            api.abort(404, "Review not found")

        if not is_admin and str(review.user_id) != str(user_id):
            api.abort(403, "Unauthorized action.")

        review_data = api.payload

        if 'user_id' in review_data:
            del review_data['user_id']

        update_review = facade.update_review(review_id, api.payload)
        return update_review

    @jwt_required()
    def delete(self, review_id):
        """Delete a notification"""
        current_user_id = get_jwt_identity()
        claims = get_jwt()
        is_admin = claims.get('is_admin', False)

        if isinstance(current_user_id, dict):
            user_id = UUID(current_user_id.get('id'))
        else:
            user_id = UUID(current_user_id)

        review = facade.get_review(review_id)
        if not review:
            api.abort(404, "Review not found")

        if not is_admin and str(review.user_id) != str(user_id):
            api.abort(403, "Unauthorized action.")

        deleted = facade.delete_review(review_id)
        if not deleted:
            api.abort(400, "Failed to delete review")

        return {"message": "Review deleted"}, 204

@api.route("/place/<string:place_id>")
@api.param("place_id", "Identifiant du lieu")
class PlaceReviewResource(Resource):
    @api.marshal_list_with(review_model)
    def get(self, place_id):
        """List the notices associated with a location"""
        return facade.get_reviews_by_place(place_id)