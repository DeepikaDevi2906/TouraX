from langchain.tools import Tool

from tools.search_hotels import hotel_search_tool
from tools.get_places import get_places_tool
from tools.emergency_support import emergency_support_tool
from tools.create_booking import booking_tool
from tools.weather_tool import weather_tool
from tools.flight_tool import flight_tool
from tools.safety_tool import safety_tool
from tools.maps_tool import maps_tool
from tools.budget_tool import budget_tool

hotel_tool=Tool(
    name="Hotel Search",
    func=hotel_search_tool,
    description="""
    Search hotels using natural language queries.

    Supports:
    - city
    - budget
    - hotel recommendations

    Example inputs:
    - Hotels in Ooty
    - Hotels in Chennai under 4000
    - Budget hotels in Madurai
    """
)

places_tool=Tool(
    name="Tourist Places",
    func=get_places_tool,
    description="""
    Get tourist places in a city.
    Input should be a city name.
    Example input:"Tourist places in Ooty"
    """
)

emergency_tool=Tool(
    name="Emergency Support",
    func=emergency_support_tool,
    description="""
Use ONLY for:
- emergency phone numbers
- ambulance numbers
- police emergency contacts
- disaster assistance

Do NOT use for:
- nearby hospitals
- nearby restaurants
- nearby hotels
- nearby places

Use Maps MCP Tool for location-based searches.
"""
)

booking_langchain_tool=Tool(
    name="Hotel Booking",
    func=booking_tool,
    description="""
    IMPORTANT:
    Use this tool immediately whenever
    the user wants to:
    - book a hotel
    - reserve a room
    - confirm a stay

    The tool already handles booking creation.

    Example inputs:
    - Book Sea View Resort
    - Reserve Luxury Palace

"""
)

weather_mcp_tool = Tool(

    name="Weather MCP Tool",

    func=weather_tool,

    description="""

Use this tool for:
- weather queries
- rain predictions
- travel weather advice
- temperature checks
- climate conditions
- travel suitability

Always use this tool when users ask about weather.

"""
)
flight_mcp_tool = Tool(
    name="Flight MCP Tool",
    func=flight_tool,
    description="""
Use this tool ONLY for flight information about a city.

IMPORTANT:
This tool DOES NOT support route searches such as:
- Coimbatore to Chennai
- Delhi to Mumbai

This tool ONLY accepts one city and returns flight information associated with that city.

Always use the tool result directly.
Do not assume missing route information.
"""
)

safety_mcp_tool = Tool(

    name="Safety MCP Tool",

    func=safety_tool,

    description="""
Use this tool for:
- city safety
- travel safety
- women traveler safety
- emergency information
- safety score
"""
)

maps_mcp_tool = Tool(

    name="Maps MCP Tool",

    func=maps_tool,

    description="""
Use for:
- hospitals near a city
- restaurants near a city
- hotels near a city
- police stations near a city
- ATMs near a city
- pharmacies near a city
- distance between cities
- travel time

ALWAYS use this tool for nearby place searches.
"""
)

budget_mcp_tool = Tool(
    name="Budget MCP Tool",
    func=budget_tool,
    description="""
Use this tool for:

- trip budget planning
- travel budget estimation
- itinerary cost calculation
- affordability analysis
- travel expense calculation

ALWAYS use this tool when the user mentions:
- budget
- cost
- expenses
- affordability
- planning a trip with a specific amount

Examples:

Plan a 3 day trip to Ooty with 25000 budget

Can I visit Ooty with 15000?

Estimate the cost of a trip to Chennai

Trip budget for Ooty
"""
)

all_tools=[
    hotel_tool,
    places_tool,
    emergency_tool,
    booking_langchain_tool,
    weather_mcp_tool,
    flight_mcp_tool,
    safety_mcp_tool,
    maps_mcp_tool,
    budget_mcp_tool
]
