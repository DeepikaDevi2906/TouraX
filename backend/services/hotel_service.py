from models.hotel_model import Hotel
from extensions import db


def get_all_hotels():

    hotels = Hotel.query.all()

    return hotels


def search_hotels(city=None, max_price=None):

    query = Hotel.query

    if city:

        query = query.filter(
            Hotel.city.ilike(city)
        )

    if max_price:

        query = query.filter(
            Hotel.price <= max_price
        )

    return query.all()


def create_hotel(name, city, price, rating):

    hotel = Hotel(
        name=name,
        city=city,
        price=price,
        rating=rating
    )

    db.session.add(hotel)

    db.session.commit()

    return hotel

def get_hotel_by_name(hotel_name):

    hotel = Hotel.query.filter(
        Hotel.name.ilike(f"%{hotel_name}%")
    ).first()

    return hotel
def get_hotel_by_id(hotel_id):

    hotel = Hotel.query.get(hotel_id)

    return hotel