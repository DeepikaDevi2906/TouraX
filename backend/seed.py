from app import app
from extensions import db

from models.hotel_model import Hotel


hotels = [

    Hotel(
        name="Sea View Resort",
        city="Chennai",
        price=2500,
        rating=4.3
    ),

    Hotel(
        name="Hill Top Hotel",
        city="Ooty",
        price=3200,
        rating=4.5
    ),

    Hotel(
        name="Budget Stay",
        city="Ooty",
        price=1800,
        rating=4.0
    ),

    Hotel(
        name="Luxury Palace",
        city="Chennai",
        price=5000,
        rating=4.8
    ),

    Hotel(
        name="Green Valley Resort",
        city="Kodaikanal",
        price=3500,
        rating=4.6
    )
]


with app.app_context():

    db.session.add_all(hotels)

    db.session.commit()

    print("Hotels added successfully!")