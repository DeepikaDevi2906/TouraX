from models.booking_model import Booking
from extensions import db


def create_booking(user_id, hotel_id):

    booking = Booking(
        user_id=user_id,
        hotel_id=hotel_id,
        status="Pending Payment"
    )

    db.session.add(booking)

    db.session.commit()

    return booking


def get_all_bookings():

    return Booking.query.all()


def get_booking_by_id(booking_id):

    return Booking.query.get(booking_id)

def update_booking_status(
    booking_id,
    new_status
):

    booking = Booking.query.get(booking_id)

    if not booking:
        return None

    booking.status = new_status

    db.session.commit()

    return booking

def get_user_bookings(user_id):

    return Booking.query.filter_by(
        user_id=user_id
    ).all()

