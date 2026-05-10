from extensions import db

class Booking(db.Model):

    __tablename__ = "bookings"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    hotel_id = db.Column(
        db.Integer,
        db.ForeignKey("hotels.id"),
        nullable=False
    )

    status = db.Column(
        db.String(50),
        default="Pending Payment"
    )