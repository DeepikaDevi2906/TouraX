from mcp.server.fastmcp import FastMCP
import requests

from dotenv import load_dotenv
import os

load_dotenv()

ORS_API_KEY = os.getenv("ORS_API_KEY")

mcp = FastMCP("maps")

def get_coordinates(place):

    url = "https://api.openrouteservice.org/geocode/search"

    params = {
        "api_key": ORS_API_KEY,
        "text": place,
        "size": 1
    }

    response = requests.get(
        url,
        params=params,
        timeout=10
    )

    if response.status_code != 200:
        raise Exception(
            f"Geocoding failed ({response.status_code})"
        )

    data = response.json()

    if (
        "features" not in data
        or len(data["features"]) == 0
    ):
        raise Exception(
            f"No coordinates found for {place}"
        )

    return data["features"][0]["geometry"]["coordinates"]


@mcp.tool()
def get_distance(
    origin: str,
    destination: str
):

    try:

        origin_coords = get_coordinates(origin)

        destination_coords = get_coordinates(destination)

        url = (
            "https://api.openrouteservice.org/"
            "v2/directions/driving-car"
        )

        headers = {
            "Authorization": ORS_API_KEY,
            "Content-Type": "application/json"
        }

        body = {
            "coordinates": [
                origin_coords,
                destination_coords
            ]
        }

        response = requests.post(
            url,
            json=body,
            headers=headers,
            timeout=20
        )

        if response.status_code != 200:

            return {
                "error":
                    f"Routing API failed ({response.status_code})"
            }

        data = response.json()

        summary = data["routes"][0]["summary"]

        distance_km = round(
            summary["distance"] / 1000,
            2
        )

        duration_hours = round(
            summary["duration"] / 3600,
            2
        )

        return {

            "origin": origin,

            "destination": destination,

            "distance_km": distance_km,

            "travel_time_hours": duration_hours
        }

    except Exception as e:

        return {

            "error": str(e)
        }

if __name__ == "__main__":

    mcp.run()
