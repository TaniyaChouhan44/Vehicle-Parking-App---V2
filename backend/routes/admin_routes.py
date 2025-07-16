from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from models import User, ParkingSpot, db
from flask_jwt_extended import get_jwt_identity


admin_bp = Blueprint('admin', __name__)

# Admin Dashboard
@admin_bp.route('/dashboard', methods=['GET'])
def dashboard():
    return jsonify({"msg": "Welcome to the admin dashboard!"})


# All Users
@admin_bp.route('/users', methods=['GET'])
@jwt_required()
def get_all_users():
    current_user_id = get_jwt_identity()
    # Optionally verify admin user with ID

    users = User.query.all()
    user_list = [{
        "id": u.id,
        "username": u.username,
        "fname": u.fname,
        "lname": u.lname,
        "email": u.email,
        "role": u.role.name
    } for u in users]

    return jsonify(user_list), 200


# Parking Spots
@admin_bp.route('/spots', methods=['GET'])
def get_spots():
    spots = ParkingSpot.query.all()
    return jsonify([
        {
            "id": spot.id,
            "lot_id": spot.lot_id,
            "spot_number": spot.spot_number,
            "status": spot.status
        } for spot in spots
    ]), 200

@admin_bp.route('/spots', methods=['POST'])
def add_spot():
    data = request.get_json()
    spot = ParkingSpot(
        lot_id=data['lot_id'],
        spot_number=data['spot_number'],
        status=data['status']
    )
    db.session.add(spot)
    db.session.commit()
    return jsonify({"msg": "Spot created"}), 201
