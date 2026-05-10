from langchain.tools import Tool

from tools.search_hotels import hotel_search_tool
from tools.get_places import get_places_tool
from tools.emergency_support import emergency_support_tool
from tools.create_booking import booking_tool


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
    Get emergency hospitals,police or ambulance support.
    Example input:"I need emergency support in Ooty
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

all_tools=[
    hotel_tool,
    places_tool,
    emergency_tool,
    booking_langchain_tool
]
