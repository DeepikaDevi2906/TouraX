from extensions import db


class Hotel(db.Model):

    __tablename__ = "hotels"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)

    city = db.Column(db.String(100), nullable=False)

    price = db.Column(db.Float, nullable=False)

    rating = db.Column(db.Float, nullable=False)

    bookings = db.relationship(
        "Booking",
        backref="hotel",
        lazy=True
    )