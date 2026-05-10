from extensions import db


class Payment(db.Model):

    __tablename__ = "payments"

    id = db.Column(db.Integer, primary_key=True)

    booking_id = db.Column(
        db.Integer,
        db.ForeignKey("bookings.id"),
        nullable=False
    )

    amount = db.Column(db.Float, nullable=False)

    payment_status = db.Column(
        db.String(50),
        default="Pending"
    )

    payment_method = db.Column(db.String(50))