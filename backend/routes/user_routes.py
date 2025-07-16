from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
from models import ParkingLot, db

user_bp = Blueprint('user', __name__)

@user_bp.route('/dashboard', methods=['GET'])
def user_dashboard():
    return jsonify({"msg": "Welcome to the user dashboard!"})


@user_bp.route('/available-lots', methods=['GET'])
@jwt_required()
def get_available_lots():
    try:
        lots = ParkingLot.query.all()
        return jsonify([
            {
                "id": lot.id,
                "prime_location_name": lot.prime_location_name,
                "price": lot.price,
                "address": lot.address,
                "pin_code": lot.pin_code,
                "number_of_spots": lot.number_of_spots
            } for lot in lots
        ]), 200
    except Exception as e:
        print("Error fetching parking lots:", e)
        return jsonify({"msg": "Server error"}), 500
