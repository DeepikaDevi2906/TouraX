from mcp.server.fastmcp import FastMCP
import requests

mcp = FastMCP("weather")

API_KEY = "d0ad185db06108b652e90446ba564bb9"


@mcp.tool()
def get_weather(city: str):

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={API_KEY}&units=metric"
    )

    try:

        response = requests.get(url)

        data = response.json()

        return {

            "city": city,

            "temperature": data["main"]["temp"],

            "condition": data["weather"][0]["description"],

            "humidity": data["main"]["humidity"]
        }

    except Exception as e:

        return {

            "error": str(e)
        }


if __name__ == "__main__":
    mcp.run()