import { useEffect, useState } from "react";

import { getHotels } from "../services/bookingService";

import HotelCard from "../components/HotelCard";


function HotelsPage() {

    const [hotels, setHotels] = useState([]);


    useEffect(() => {

        fetchHotels();

    }, []);


    const fetchHotels = async () => {

        const data = await getHotels();

        setHotels(data);
    };


    return (

    <div>

        <h1 className="page-title">
            Explore Hotels
        </h1>

        <div className="hotels-container">

            {
                hotels.map((hotel) => (

                    <HotelCard
                        key={hotel.id}
                        hotel={hotel}
                    />
                ))
            }

        </div>

    </div>
);
}

export default HotelsPage;