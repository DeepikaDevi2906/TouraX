import { Link, useNavigate }
from "react-router-dom";

import { useAuth }
from "../context/AuthContext";


function Navbar() {

    const { user, logout } = useAuth();

    const navigate = useNavigate();


    const handleLogout = () => {

        logout();

        navigate("/login");
    };


    return (

    <nav className="navbar">

        <h2>TouraX</h2>

        <div className="nav-links">

            <Link to="/">
                Home
            </Link>

            <Link to="/hotels">
                Hotels
            </Link>

            <Link to="/chat">
                AI Chat
            </Link>

            {
                user && (

                    <Link to="/bookings">
                        Bookings
                    </Link>
                )
            }

            {
                !user ? (

                    <>

                        <Link to="/login">
                            Login
                        </Link>

                        <Link to="/register">
                            Register
                        </Link>

                    </>

                ) : (

                    <>

                        <span>
                            Welcome, {user.name}
                        </span>

                        <button
                            className="primary-btn"
                            onClick={handleLogout}
                        >
                            Logout
                        </button>

                    </>
                )
            }

        </div>

    </nav>
);
}

export default Navbar;