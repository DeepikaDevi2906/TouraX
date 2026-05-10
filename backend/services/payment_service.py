from models.payment_model import Payment
from extensions import db

from services.booking_service import (
    update_booking_status
)

def create_payment(booking_id,amount,payment_method):

    payment = Payment(
        booking_id=booking_id,
        amount=amount,
        payment_method=payment_method,
        payment_status="Success"
    )

    db.session.add(payment)

    update_booking_status(
        booking_id,
        "Confirmed"
    )

    db.session.commit()

    return payment


def get_all_payments():

    return Payment.query.all()