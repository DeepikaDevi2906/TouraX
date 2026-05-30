import asyncio

from mcp_clients.safety_client import (
    get_safety_info
)


def safety_tool(user_query):

    cities = [

        "ooty",

        "chennai",

        "coimbatore",

        "madurai",

        "mumbai",

        "delhi",

        "bangalore",

        "hyderabad"
    ]

    query = user_query.lower()

    detected_city = None

    for city in cities:

        if city in query:

            detected_city = city

            break

    if not detected_city:

        return "Please specify a city."

    try:

        result = asyncio.run(

            get_safety_info(
                detected_city
            )
        )

        return result.content[0].text

    except Exception as e:

        return f"Safety MCP Error: {str(e)}"