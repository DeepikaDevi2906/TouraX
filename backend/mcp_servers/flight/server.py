from mcp.server.fastmcp import FastMCP
import requests
from dotenv import load_dotenv
import os
import requests
load_dotenv()

mcp = FastMCP("flight")

RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")

DESTINATION_FLIGHTS = {
    "chennai": "AI574",
    "delhi": "AI302",
    "mumbai": "6E533",
    "bangalore": "UK811",
    "hyderabad": "6E6721",
    "coimbatore": "AI429",
    "madurai": "6E729"
}

TICKET_PRICES = {
    "chennai": 6200,
    "delhi": 8500,
    "mumbai": 7000,
    "bangalore": 5000,
    "hyderabad": 6500,
    "coimbatore": 4500,
    "madurai": 4000
}


@mcp.tool()
def get_destination_flight(city: str):
    """
    Get flight details and estimated ticket price for a destination city.
    """

    city = city.lower()

    if city not in DESTINATION_FLIGHTS:
        return {
            "error": "City not supported"
        }

    flight_number = DESTINATION_FLIGHTS[city]

    estimated_price = TICKET_PRICES.get(city, 5000)

    url = f"https://aerodatabox.p.rapidapi.com/flights/number/{flight_number}"

    headers = {
        "x-rapidapi-key": RAPIDAPI_KEY,
        "x-rapidapi-host": "aerodatabox.p.rapidapi.com"
    }

    params = {
        "withAircraftImage": "false",
        "withLocation": "false",
        "withFlightPlan": "false"
    }

    try:

        response = requests.get(
            url,
            headers=headers,
            params=params
        )

        if response.status_code != 200:
            return {
                "error": f"API request failed ({response.status_code})"
            }

        data = response.json()

        result = []

        for flight in data[:3]:

            result.append({

                "airline": flight.get(
                    "airline", {}
                ).get("name"),

                "flight_number": flight.get(
                    "number"
                ),

                "status": flight.get(
                    "status"
                ),

                "departure_airport": flight.get(
                    "departure", {}
                ).get("airport", {})
                .get("name"),

                "arrival_airport": flight.get(
                    "arrival", {}
                ).get("airport", {})
                .get("name"),

                "departure_time": flight.get(
                    "departure", {}
                ).get("scheduledTime", {})
                .get("local"),

                "arrival_time": flight.get(
                    "arrival", {}
                ).get("scheduledTime", {})
                .get("local"),

                "estimated_ticket_price": estimated_price
            })

        return result

    except Exception as e:
        return {
            "error": str(e)
        }


if __name__ == "__main__":
    mcp.run()
   
   
