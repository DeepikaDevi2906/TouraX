import asyncio

from mcp_clients.weather_client import (
    get_weather
)


def weather_tool(user_query):

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

    if not detected_city:

        return "Please specify a city."


    try:

        result = asyncio.run(

            get_weather(
                detected_city
            )
        )

        return result.content[0].text

    except Exception as e:

        return f"Weather MCP Error: {str(e)}"