import asyncio
import re

from mcp_clients.weather_client import (
    get_weather
)

from mcp_clients.maps_client import (
    get_distance
)

from mcp_clients.budget_client import (
    estimate_trip_budget
)


def budget_tool(user_query):

    query = user_query.lower()

    cities = [

        "ooty",

        "chennai",

        "coimbatore",

        "madurai",

        "bangalore",

        "hyderabad",

        "mumbai",

        "delhi"
    ]

    destination = None

    for city in cities:

        if city in query:

            destination = city

            break

    if not destination:

        return "Please specify a destination city."

    # Extract budget

    budget_match = re.search(

        r'(\d{4,6})',

        query
    )

    budget = (

        int(budget_match.group(1))

        if budget_match

        else 10000
    )

    # Extract days

    days_match = re.search(

        r'(\d+)\s*day',

        query
    )

    days = (

        int(days_match.group(1))

        if days_match

        else 2
    )

    try:

        # Weather MCP

        weather_result = asyncio.run(

            get_weather(
                destination
            )
        )

        weather_text = (

            weather_result.content[0].text
        )

        # Maps MCP

        distance_result = asyncio.run(

            get_distance(

                "chennai",

                destination
            )
        )

        distance_text = (

            distance_result.content[0].text
        )

        import json

        distance_data = json.loads(
            distance_text
        )

        distance_km = distance_data.get(
            "distance_km",
            200
        )

        # Budget MCP

        result = asyncio.run(

            estimate_trip_budget(

                destination,

                budget,

                days,

                weather_text,

                distance_km
            )
        )

        return result.content[0].text

    except Exception as e:

        return f"Budget MCP Error: {str(e)}"