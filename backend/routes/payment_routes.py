from flask import Blueprint, request, jsonify

from services.payment_service import create_payment,get_all_payments

payment_bp = Blueprint("payment_bp", __name__)


@payment_bp.route("/payment", methods=["POST"])
def payment():

    data = request.json

    booking_id = data.get("booking_id")

    amount = data.get("amount")

    payment_method = data.get("payment_method")

    payment = create_payment(
        booking_id=booking_id,
        amount=amount,
        payment_method=payment_method
    )

    return jsonify({
        "payment_id": payment.id,
        "payment_status": payment.payment_status
    })


@payment_bp.route("/payments", methods=["GET"])
def payments():

    payments = get_all_payments()

    payment_list = []

    for payment in payments:

        payment_list.append({
            "payment_id": payment.id,
            "booking_id": payment.booking_id,
            "amount": payment.amount,
            "payment_status": payment.payment_status
        })

    return jsonify(payment_list)