from services.hotel_service import get_hotel_by_name
from services.booking_service import create_booking

from tools.payment_redirect import payment_redirect_tool



def booking_tool(user_query):

    hotel_names = [
        "sea view resort",
        "luxury palace"
    ]

    query = user_query.lower()

    detected_hotel = None

    for hotel_name in hotel_names:

        if hotel_name in query:

            detected_hotel = hotel_name

            break

    if not detected_hotel:

        return "Hotel not found."

    hotel = get_hotel_by_name(
        detected_hotel
    )

    if not hotel:

        return "Hotel not found."

    booking = create_booking(
        user_id=1,
        hotel_id=hotel.id
    )

    payment_data = payment_redirect_tool(
        booking_id=booking.id,
        hotel_id=hotel.id
    )

    return (
    f"Booking created for "
    f"{hotel.name}.\n"
    f"Booking ID: {booking.id}\n"
    f"Status: {booking.status}\n"
    f"Payment Link: "
    f"http://localhost:3000"
    f"{payment_data['redirect_url']}"
)