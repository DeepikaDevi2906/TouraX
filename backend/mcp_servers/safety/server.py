from mcp.server.fastmcp import FastMCP

mcp = FastMCP("safety")


CITY_SAFETY = {

    "ooty": 88,

    "chennai": 82,

    "coimbatore": 85,

    "madurai": 78,

    "mumbai": 75,

    "delhi": 65,

    "bangalore": 84,

    "hyderabad": 83
}


@mcp.tool()
def get_safety_info(city: str):

    city = city.lower()

    if city not in CITY_SAFETY:

        return {

            "error": "City not supported"
        }

    score = CITY_SAFETY[city]

    if score >= 85:
        level = "Very Safe"
    elif score >= 75:
        level = "Safe"
    elif score >= 60:
        level = "Moderately Safe"
    else:
        level = "Use Caution"

    return {

        "city": city.title(),

        "safety_score": score,

        "safety_level": level,

        "emergency_number": "112",

        "recommendation":
            f"{city.title()} is generally {level.lower()} for travelers."
    }


if __name__ == "__main__":

    mcp.run()