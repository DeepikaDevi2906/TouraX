from mcp import ClientSession
from mcp.client.stdio import (
    stdio_client,
    StdioServerParameters
)


async def get_distance(
    origin: str,
    destination: str
):

    server_params = StdioServerParameters(

        command="python",

        args=[
            "mcp_servers/maps/server.py"
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

                "get_distance",

                {
                    "origin": origin,
                    "destination": destination
                }
            )

            return result
        
async def get_nearby_places(
    place: str,
    category: str
):

    server_params = StdioServerParameters(

        command="python",

        args=[
            "mcp_servers/maps/server.py"
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

                "get_nearby_places",

                {
                    "place": place,

                    "category": category
                }
            )

            return result