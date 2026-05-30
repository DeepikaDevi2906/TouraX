import asyncio

from mcp import ClientSession
from mcp.client.stdio import (
    stdio_client,
    StdioServerParameters
)


async def get_destination_flight(city: str):

    server_params = StdioServerParameters(

        command="python",

        args=[
            "mcp_servers/flight/server.py"
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

                "get_destination_flight",

                {
                    "city": city
                }
            )

            return result