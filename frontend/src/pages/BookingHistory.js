import { useEffect, useState } from "react";

import { getBookings } from "../services/bookingService";

import { useAuth } from "../context/AuthContext";


function BookingHistory() {

    const [bookings, setBookings] =
        useState([]);

    const { user } = useAuth();


    useEffect(() => {

        if (user) {

            fetchBookings();
        }

    }, [user]);


    const fetchBookings =
        async () => {

        try {

            const data =
                await getBookings(
                    user.id
                );

            // SAFETY CHECK
            if (Array.isArray(data)) {

                setBookings(data);

            } else {

                setBookings([]);
            }

        } catch (error) {

            console.log(error);

            setBookings([]);
        }
    };


    return (

        <div className="history-container">

            <h1 className="page-title">
                Booking History
            </h1>


            {
                bookings.length === 0 ? (

                    <p>
                        No bookings found.
                    </p>

                ) : (

                    bookings.map((booking) => (

                        <div
                            key={booking.booking_id}

                            className="history-card"
                        >

                            <h3>
                                Booking ID:
                                {" "}
                                {booking.booking_id}
                            </h3>

                            <p>
                                User ID:
                                {" "}
                                {booking.user_id}
                            </p>

                            <p>
                                Hotel ID:
                                {" "}
                                {booking.hotel_id}
                            </p>

                            <p>

                                Status:

                                <span
                                    className={
                                        booking.status ===
                                        "Confirmed"

                                        ? "status-confirmed"

                                        : "status-pending"
                                    }
                                >

                                    {" "}
                                    {booking.status}

                                </span>

                            </p>

                        </div>
                    ))
                )
            }

        </div>
    );
}

export default BookingHistory;