import asyncio

from mcp_clients.maps_client import (
    get_distance,
    get_nearby_places
)


def maps_tool(user_query):

    query = user_query.lower()

    cities = [

        "chennai",

        "ooty",

        "coimbatore",

        "madurai",

        "bangalore",

        "hyderabad",

        "mumbai",

        "delhi"
    ]

    categories = [

        "hospital",

        "restaurant",

        "atm",

        "hotel",

        "police",

        "pharmacy"
    ]

    # -------------------------
    # Nearby Places Search
    # -------------------------

    detected_category = None

    for category in categories:

        if category in query:

            detected_category = category

            break

    if detected_category:

        detected_place = None

        for city in cities:

            if city in query:

                detected_place = city

                break

        if not detected_place:

            return """
Please specify a location.

Examples:
- Hospitals near Ooty
- Restaurants near Chennai
- Hotels near Coimbatore
"""

        try:

            result = asyncio.run(

                get_nearby_places(

                    detected_place,

                    detected_category
                )
            )

            return result.content[0].text

        except Exception as e:

            return f"Maps MCP Error: {str(e)}"

    # -------------------------
    # Distance Search
    # -------------------------

    found_cities = []

    for city in cities:

        if city in query:

            found_cities.append(city)

    if len(found_cities) >= 2:

        try:

            result = asyncio.run(

                get_distance(

                    found_cities[0],

                    found_cities[1]
                )
            )

            return result.content[0].text

        except Exception as e:

            return f"Maps MCP Error: {str(e)}"

    # -------------------------
    # Help Message
    # -------------------------

    return """
Supported Maps Queries:

Distance:
- Distance from Chennai to Ooty
- Distance from Bangalore to Chennai
- Travel from Coimbatore to Madurai

Nearby Places:
- Hospitals near Ooty
- Restaurants near Chennai
- Hotels near Coimbatore
- Police near Madurai
- Pharmacy near Bangalore
- ATM near Hyderabad
"""