from mcp import ClientSession
from mcp.client.stdio import (
    stdio_client,
    StdioServerParameters
)


async def estimate_trip_budget(
    destination: str,
    budget: int,
    days: int,
    weather: str,
    distance_km: float
):

    server_params = StdioServerParameters(

        command="python",

        args=[
            "mcp_servers/budget/server.py"
        ]
    )

    async with stdio_client(
        server_params
    ) as (read, write):

        async with ClientSession(
            read,
            write
        ) as session:

            await session.initialize()

            result = await session.call_tool(

                "estimate_trip_budget",

                {

                    "destination": destination,

                    "budget": budget,

                    "days": days,

                    "weather": weather,

                    "distance_km": distance_km
                }
            )

            return result