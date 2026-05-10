// frontend/src/components/ChatBox.js

import {
    useState,
    useEffect
} from "react";

import {
    useNavigate
} from "react-router-dom";

import MessageBubble
from "./MessageBubble";

import {
    sendMessage,
    getMessages
} from "../services/chatService";


function ChatBox() {

    const [message, setMessage] =
        useState("");

    const [messages, setMessages] =
        useState([]);

    const [loading, setLoading] =
        useState(false);

    const navigate = useNavigate();


    // ---------- LOAD OLD CHATS ----------

    useEffect(() => {

        fetchMessages();

    }, []);


    const fetchMessages = async () => {

        try {

            const data =
                await getMessages();

            setMessages(data);

        } catch (error) {

            console.log(error);
        }
    };


    // ---------- SEND MESSAGE ----------

    const handleSend = async () => {

        if (!message.trim()) return;


        const userMessage = {

            sender: "user",

            text: message
        };


        setMessages((prev) => [

            ...prev,

            userMessage
        ]);


        setLoading(true);


        try {

            const data =
                await sendMessage(
                    message
                );


            const aiMessage = {

                sender: "ai",

                text: data.message
            };


            setMessages((prev) => [

                ...prev,

                aiMessage
            ]);


            // ---------- BOOKING REDIRECT ----------

            if (data.type === "booking") {

                navigate(data.redirect_url, {

                    state: {

                        booking_id:
                            data.booking_id,

                        hotel_id:
                            data.hotel_id
                    }
                });
            }

        } catch (error) {

            console.log(error);

        } finally {

            setLoading(false);
        }


        setMessage("");
    };


    return (

        <div className="chat-page">

            <div className="chat-container">

                {
                    messages.map((msg, index) => (

                        <MessageBubble

                            key={index}

                            sender={msg.sender}

                            text={msg.text}
                        />
                    ))
                }

                {
                    loading && (

                        <MessageBubble

                            sender="ai"

                            text="Typing..."
                        />
                    )
                }

            </div>


            <div className="chat-input-container">

                <input
                    className="chat-input"

                    type="text"

                    placeholder=
                        "Ask your travel query..."

                    value={message}

                    onChange={(e) =>
                        setMessage(
                            e.target.value
                        )
                    }
                />


                <button
                    className="primary-btn"

                    onClick={handleSend}
                >
                    Send
                </button>

            </div>

        </div>
    );
}

export default ChatBox;