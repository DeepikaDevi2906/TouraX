function MessageBubble({ sender, text }) {

    return (

        <div className={`message-row ${sender}`}>

            <div
                className={`message-bubble ${sender}`}
            >

                {text}

            </div>

        </div>
    );
}

export default MessageBubble;