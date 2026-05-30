from mcp.server.fastmcp import FastMCP
import requests
from dotenv import load_dotenv
import os

load_dotenv()

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

mcp = FastMCP("weather")

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
