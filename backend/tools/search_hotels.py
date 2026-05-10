import re

from services.hotel_service import search_hotels



def hotel_search_tool(user_query):

    query = user_query.lower()

    cities = [
        "ooty",
        "chennai",
        "coimbatore",
        "madurai",
        "kodaikanal"
    ]

    detected_city = None

    for city in cities:

        if city in query:

            detected_city = city

            break

    price_match = re.search(r'(\d+)', query)

    max_price = None

    if price_match:

        max_price = int(
            price_match.group(1)
        )

    hotels = search_hotels(
        city=detected_city,
        max_price=max_price
    )

    return hotels