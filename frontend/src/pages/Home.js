import { motion } from "framer-motion";

import {
    FaRobot,
    FaHotel,
    FaPlaneDeparture
} from "react-icons/fa";

import { useNavigate } from "react-router-dom";


function Home() {

    const navigate = useNavigate();

    return (

        <div className="home-page">

            {/* ---------- HERO SECTION ---------- */}

            <div className="hero-section">

                <motion.div

                    initial={{ opacity: 0, y: 50 }}

                    animate={{ opacity: 1, y: 0 }}

                    transition={{ duration: 0.8 }}

                    className="hero-content"
                >

                    <h1 className="hero-title">
                        Explore The World With
                        <span>
                            AI Tourism Assistant ✨
                        </span>
                    </h1>

                    <p className="hero-subtitle">
                        Your intelligent travel companion for hotel booking,
                        trip planning, tourist guidance,
                        and real-time customer care.
                    </p>

                    <div className="hero-buttons">

                        <button
                            className="primary-btn"
                            onClick={() =>
                                navigate("/hotels")
                            }
                        >
                            Start Exploring
                        </button>

                        <button
                            className="secondary-btn"
                            onClick={() =>
                                navigate("/chat")
                            }
                        >
                            Chat With AI
                        </button>

                    </div>

                </motion.div>

            </div>


            {/* ---------- FEATURES ---------- */}

            <div className="features-section">

                <h2 className="section-title">
                    Why Choose Us?
                </h2>


                <div className="features-grid">

                    <motion.div

                        className="feature-card"

                        whileHover={{
                            scale: 1.05
                        }}
                    >

                        <FaRobot className="feature-icon" />

                        <h3>AI Travel Assistant</h3>

                        <p>
                            Get intelligent recommendations,
                            trip guidance and travel support.
                        </p>

                    </motion.div>


                    <motion.div

                        className="feature-card"

                        whileHover={{
                            scale: 1.05
                        }}
                    >

                        <FaHotel className="feature-icon" />

                        <h3>Smart Hotel Booking</h3>

                        <p>
                            Discover premium and budget-friendly
                            stays instantly.
                        </p>

                    </motion.div>


                    <motion.div

                        className="feature-card"

                        whileHover={{
                            scale: 1.05
                        }}
                    >

                        <FaPlaneDeparture className="feature-icon" />

                        <h3>Travel Planning</h3>

                        <p>
                            Plan memorable trips with personalized
                            travel assistance.
                        </p>

                    </motion.div>

                </div>

            </div>

        </div>
    );
}

export default Home;