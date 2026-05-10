import { useState } from "react";

import { registerUser }
from "../services/authService";


function Register() {

    const [name, setName] =
        useState("");

    const [email, setEmail] =
        useState("");

    const [password, setPassword] =
        useState("");

    const [message, setMessage] =
        useState("");

    const [loading, setLoading] =
        useState(false);


    const handleRegister = async () => {

        if (loading) return;

        setLoading(true);

        try {

            const data = await registerUser({
                name,
                email,
                password
            });

            setMessage(data.message);

        } catch (error) {

            setMessage("Registration failed");

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
                Register
            </h1>

            <input
                className="form-input"

                type="text"

                placeholder="Enter Name"

                onChange={(e) =>
                    setName(e.target.value)
                }
            />

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

                onClick={handleRegister}

                disabled={loading}

                style={{
                    width: "100%"
                }}
            >

                {
                    loading
                        ? "Registering..."
                        : "Register"
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

export default Register;