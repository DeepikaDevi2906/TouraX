from mcp.server.fastmcp import FastMCP

mcp = FastMCP("budget")


@mcp.tool()
def estimate_trip_budget(
    destination: str,
    budget: int,
    days: int,
    weather: str,
    distance_km: float
):

    hotel_cost = days * 2500

    food_cost = days * 1000

    travel_cost = max(
        1000,
        int(distance_km * 5)
    )

    misc_cost = days * 500

    total_cost = (

        hotel_cost

        + food_cost

        + travel_cost

        + misc_cost
    )

    remaining = budget - total_cost

    recommendation = (

        "Budget is sufficient"

        if remaining >= 0

        else "Budget may not be sufficient"
    )

    return {

        "destination": destination,

        "trip_days": days,

        "weather": weather,

        "travel_cost": travel_cost,

        "hotel_cost": hotel_cost,

        "food_cost": food_cost,

        "misc_cost": misc_cost,

        "total_cost": total_cost,

        "remaining_budget": remaining,

        "recommendation": recommendation
    }


if __name__ == "__main__":

    mcp.run()