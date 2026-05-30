from mcp import ClientSession
from mcp.client.stdio import (
    stdio_client,
    StdioServerParameters
)


async def get_safety_info(city: str):

    server_params = StdioServerParameters(

        command="python",

        args=[
            "mcp_servers/safety/server.py"
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

                "get_safety_info",

                {
                    "city": city
                }
            )

            return result