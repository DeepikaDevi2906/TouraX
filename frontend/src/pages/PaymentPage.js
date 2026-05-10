import { useEffect, useState } from "react";

import {
    useNavigate,
    useParams,
} from "react-router-dom";

import {
    getHotelById,
    makePayment,
    getBookingById
} from "../services/bookingService";


function PaymentPage() {

    const navigate = useNavigate();

    const { bookingId } = useParams();

    const [hotel, setHotel] =
        useState(null);

    const [booking, setBooking] =
        useState(null);

    const [message, setMessage] =
        useState("");

    const [paymentDone,
           setPaymentDone] =
        useState(false);


    useEffect(() => {

        fetchBookingAndHotel();

    }, []);


    const fetchBookingAndHotel =
        async () => {

        try {

            // -------------------
            // GET BOOKING
            // -------------------

            const bookingData =
                await getBookingById(
                    bookingId
                );

            setBooking(bookingData);

            // -------------------
            // GET HOTEL
            // -------------------

            const hotelData =
                await getHotelById(
                    bookingData.hotel_id
                );

            setHotel(hotelData);

        } catch (error) {

            console.log(error);
        }
    };


    const handlePayment =
        async () => {

        try {

            const data =
                await makePayment(

                    bookingId,

                    hotel.price
                );


            setMessage(
                `Payment ${data.payment_status}`
            );

            setPaymentDone(true);

        } catch (error) {

            console.log(error);
        }
    };


    if (!hotel || !booking) {

        return <h2>Loading...</h2>;
    }


    return (

        <div className="booking-container">

            <h1
                style={{
                    marginBottom: "20px"
                }}
            >
                Payment Page
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
                <strong>Booking ID:</strong>
                {bookingId}
            </p>

            <p>
                <strong>Status:</strong>
                {booking.status}
            </p>


            {
                !paymentDone ? (

                    <button
                        className="primary-btn"

                        onClick={handlePayment}

                        style={{
                            width: "100%",
                            marginTop: "20px"
                        }}
                    >
                        Pay Now
                    </button>

                ) : (

                    <button
                        className="primary-btn"

                        onClick={() =>
                            navigate("/bookings")
                        }

                        style={{
                            width: "100%",
                            marginTop: "20px"
                        }}
                    >
                        Go To My Bookings
                    </button>
                )
            }


            {
                message && (

                    <p className="success-message">

                        {message}

                    </p>
                )
            }

        </div>
    );
}

export default PaymentPage;