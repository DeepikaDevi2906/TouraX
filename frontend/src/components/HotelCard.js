import { useNavigate } from "react-router-dom";


function HotelCard({ hotel }) {

    const navigate = useNavigate();


    const handleBooking = () => {

        navigate("/booking", {
            state: {
                hotel
            }
        });
    };


    return (

    <div className="hotel-card">

        <h2>{hotel.name}</h2>

        <p>City: {hotel.city}</p>

        <p>Price: ₹{hotel.price}</p>

        <p>Rating: {hotel.rating}</p>

        <button
            className="primary-btn"
            onClick={handleBooking}
        >
            Book Now
        </button>

    </div>
);
}

export default HotelCard;