from flask import Blueprint, request, jsonify

from services.hotel_service import get_all_hotels,search_hotels,get_hotel_by_id


from services.booking_service import (
    create_booking,
    get_all_bookings,get_user_bookings
)
from services.booking_service import (
    get_booking_by_id
)

booking_bp = Blueprint("booking_bp", __name__)


@booking_bp.route("/hotels", methods=["GET"])
def hotels():

    city = request.args.get("city")

    max_price = request.args.get("max_price")

    if max_price:
        max_price = float(max_price)

    hotels = search_hotels(
        city=city,
        max_price=max_price
    )

    hotel_list = []

    for hotel in hotels:

        hotel_list.append({
            "id": hotel.id,
            "name": hotel.name,
            "city": hotel.city,
            "price": hotel.price,
            "rating": hotel.rating
        })

    return jsonify(hotel_list)


@booking_bp.route("/book", methods=["POST"])
def book_hotel():

    data = request.json

    user_id = data.get("user_id")

    hotel_id = data.get("hotel_id")

    booking = create_booking(
        user_id=user_id,
        hotel_id=hotel_id
    )

    return jsonify({
        "booking_id": booking.id,
        "status": booking.status
    })


@booking_bp.route("/bookings/<int:user_id>",
                  methods=["GET"])
def bookings(user_id):

    bookings = get_user_bookings(user_id)

    booking_list = []

    for booking in bookings:

        booking_list.append({
            "booking_id": booking.id,
            "user_id": booking.user_id,
            "hotel_id": booking.hotel_id,
            "status": booking.status
        })

    return jsonify(booking_list)

@booking_bp.route(
    "/hotel/<int:hotel_id>",
    methods=["GET"]
)
def get_hotel(hotel_id):

    hotel = get_hotel_by_id(
        hotel_id
    )

    if not hotel:

        return jsonify({
            "message": "Hotel not found"
        }), 404


    return jsonify({

        "id": hotel.id,

        "name": hotel.name,

        "city": hotel.city,

        "price": hotel.price,

        "rating": hotel.rating
    })

@booking_bp.route(
    "/booking/<int:booking_id>",
    methods=["GET"]
)
def single_booking(booking_id):

    booking = get_booking_by_id(
        booking_id
    )

    if not booking:

        return jsonify({
            "message": "Booking not found"
        }), 404

    return jsonify({

        "booking_id": booking.id,

        "hotel_id": booking.hotel_id,

        "user_id": booking.user_id,

        "status": booking.status
    })