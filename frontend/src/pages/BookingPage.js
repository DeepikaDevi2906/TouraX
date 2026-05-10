import { useLocation, useNavigate } from "react-router-dom";

import { createBooking } from "../services/bookingService";

import { useAuth } from "../context/AuthContext";
function BookingPage() {

    const location = useLocation();

    const navigate = useNavigate();

    const hotel = location.state?.hotel;

    const { user } = useAuth();
    const handleConfirmBooking = async () => {

        const bookingData = {
            user_id:user.id,
            hotel_id: hotel.id
        };

        const response = await createBooking(
            bookingData
        );

        navigate("/payment", {
            state: {
                booking: response,
                hotel
            }
        });
    };


    return (

    <div className="booking-container">

        <h1
            style={{
                marginBottom: "20px"
            }}
        >
            Booking Details
        </h1>

        <h2>{hotel.name}</h2>

        <p>
            <strong>City:</strong>
            {hotel.city}
        </p>

        <p>
            <strong>Price:</strong>
            ₹{hotel.price}
        </p>

        <p>
            <strong>Rating:</strong>
            {hotel.rating}
        </p>

        <button
            className="primary-btn"

            onClick={handleConfirmBooking}

            style={{
                width: "100%",
                marginTop: "20px"
            }}
        >
            Confirm Booking
        </button>

    </div>
);
}

export default BookingPage;