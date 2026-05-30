import asyncio
from mcp_clients.flight_client import get_destination_flight


def flight_tool(user_query):

    query = user_query.lower()

    cities = [
        "chennai",
        "delhi",
        "mumbai",
        "bangalore",
        "hyderabad",
        "coimbatore",
        "madurai"
    ]

    detected_city = None

    for city in cities:

        if city in query:

            detected_city = city

            break

    if not detected_city:

        return """
Please specify a city.

Supported cities:
- Chennai
- Delhi
- Mumbai
- Bangalore
- Hyderabad
- Coimbatore
- Madurai
"""

    try:

        result = asyncio.run(
            get_destination_flight(
                detected_city
            )
        )

        return result.content[0].text

    except Exception as e:

        return f"Flight MCP Error: {str(e)}"