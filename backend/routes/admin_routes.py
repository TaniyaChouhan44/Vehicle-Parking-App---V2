from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from models import User, ParkingSpot, db, ParkingLot
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


# Parking Lots
@admin_bp.route('/parking_lots', methods=['POST'])
def create_parking_lot():
    data = request.get_json()
    
    # Create a new parking lot
    new_ParkingLot = ParkingLot(
        prime_location_name=data['name'],
        price=data['price'],
        address=data['address'],
        pin_code=data['pin_code'],
        number_of_spots=data['number_of_spots']
    )
    db.session.add(new_ParkingLot)
    db.session.commit()

    # Auto-generate parking spots
    for i in range(1, new_ParkingLot.number_of_spots + 1):
        spot = ParkingSpot(
            lot_id=new_ParkingLot.id,
            spot_number=f"Spot {i}",
            status='A'
        )
        db.session.add(spot)

    db.session.commit()

    return jsonify({"msg": "Parking lot created successfully!", 'lot_id': new_ParkingLot.id,
                     "created_at": new_ParkingLot.created_at.isoformat()}), 201


# Parking Spots
@admin_bp.route('/parking_spots', methods=['POST'])
def create_parking_spots():
    data = request.get_json()
    new_spots = []

    for i in range(1, data['number_of_spots'] + 1):
        spot = ParkingSpot(
            lot_id=data['lot_id'],
            spot_number=f"Spot {i}",
            status='A'
        )
        db.session.add(spot)
        new_spots.append(spot)

    db.session.commit()

    return jsonify({"msg": "Parking spots created successfully!", "spots": [spot.id for spot in new_spots]}), 201