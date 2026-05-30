from mcp import ClientSession
from mcp.client.stdio import (
    stdio_client,
    StdioServerParameters
)


async def get_weather(city: str):

    server_params = StdioServerParameters(

        command="python",

        args=[
            "mcp_servers/weather/server.py"
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

                "get_weather",

                {
                    "city": city
                }
            )

            return result


if __name__ == "__main__":

    import asyncio

    result = asyncio.run(
        get_weather("ooty")
    )

    print(result)