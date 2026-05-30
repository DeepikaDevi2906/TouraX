def payment_redirect_tool(booking_id,hotel_id):

    return {

        "type": "payment_redirect",

        "booking_id": booking_id,

        "hotel_id": hotel_id,

        "redirect_url":
            f"/payment/{booking_id}"
    }