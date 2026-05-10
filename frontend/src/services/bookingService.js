import API from "./api";
import axios from "axios";


// -----------------------------------
// GET ALL HOTELS
// -----------------------------------

export const getHotels = async () => {

    const response = await API.get(
        "/hotels"
    );

    return response.data;
};


// -----------------------------------
// CREATE BOOKING
// -----------------------------------

export const createBooking =
    async (bookingData) => {

    const response = await API.post(

        "/book",

        bookingData
    );

    return response.data;
};


// -----------------------------------
// GET USER BOOKINGS
// RETURNS ARRAY
// -----------------------------------

export const getBookings =
    async (userId) => {

    const response = await API.get(

        `/bookings/${userId}`
    );

    return response.data;
};


// -----------------------------------
// GET SINGLE BOOKING
// RETURNS OBJECT
// -----------------------------------

export const getBookingById =
    async (bookingId) => {

    const response = await axios.get(

        `http://localhost:5000/booking/${bookingId}`
    );

    return response.data;
};


// -----------------------------------
// MAKE PAYMENT
// -----------------------------------

export const makePayment =
    async (
        bookingId,
        amount
    ) => {

    const response = await API.post(

        "/payment",

        {
            booking_id: bookingId,

            amount: amount,

            payment_method: "UPI"
        }
    );

    return response.data;
};


// -----------------------------------
// GET HOTEL BY ID
// -----------------------------------

export const getHotelById =
    async (hotelId) => {

    const response = await API.get(

        `/hotel/${hotelId}`
    );

    return response.data;
};