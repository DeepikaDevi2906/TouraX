import { useState } from "react";

import { loginUser }
from "../services/authService";

import { useAuth }
from "../context/AuthContext";

import { useNavigate }
from "react-router-dom";


function Login() {

    const [email, setEmail] =
        useState("");

    const [password, setPassword] =
        useState("");

    const [message, setMessage] =
        useState("");

    const [loading, setLoading] =
        useState(false);

    const { login } = useAuth();

    const navigate = useNavigate();


    const handleLogin = async () => {

        if (loading) return;

        setLoading(true);

        try {

            const data = await loginUser({
                email,
                password
            });

            if (data.success) {

                login(

                    {
                        id: data.user_id,
                        name: data.name
                    },

                    data.token
                );

                navigate("/");
            }

            setMessage(data.message);

        } catch (error) {

            setMessage("Login failed");

        } finally {

            setLoading(false);
        }
    };


    return (

        <div className="auth-container">

            <h1
                style={{
                    marginBottom: "20px",
                    textAlign: "center"
                }}
            >
                Login
            </h1>

            <input
                className="form-input"

                type="email"

                placeholder="Enter Email"

                onChange={(e) =>
                    setEmail(e.target.value)
                }
            />

            <input
                className="form-input"

                type="password"

                placeholder="Enter Password"

                onChange={(e) =>
                    setPassword(e.target.value)
                }
            />

            <button
                className="primary-btn"

                onClick={handleLogin}

                disabled={loading}

                style={{
                    width: "100%"
                }}
            >

                {
                    loading
                        ? "Logging in..."
                        : "Login"
                }

            </button>

            {
                message && (

                    <p
                        style={{
                            marginTop: "15px",
                            textAlign: "center"
                        }}
                    >
                        {message}
                    </p>
                )
            }

        </div>
    );
}

export default Login;