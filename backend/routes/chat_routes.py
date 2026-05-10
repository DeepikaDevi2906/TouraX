# backend/routes/chat_routes.py

from flask import Blueprint,request,jsonify

from flask_jwt_extended import jwt_required, get_jwt_identity

from services.ai_service import generate_ai_response


from services.chat_service import save_message,get_user_messages

chat_bp = Blueprint(
    "chat_bp",
    __name__
)

@chat_bp.route(
    "/chat",
    methods=["POST"]
)
@jwt_required()
def chat():

    user_id = get_jwt_identity()

    data = request.json

    message = data.get("message")

    save_message(

        user_id=user_id,

        sender="user",

        message=message
    )


    ai_reply = generate_ai_response(
        message
    )


    save_message(

        user_id=user_id,

        sender="ai",

        message=ai_reply["message"]
    )


    return jsonify(ai_reply)

@chat_bp.route(
    "/messages",
    methods=["GET"]
)
@jwt_required()
def get_messages():

    user_id = get_jwt_identity()

    messages = get_user_messages(
        user_id
    )

    chat_history = []


    for msg in messages:

        chat_history.append({

            "sender": msg.sender,

            "text": msg.message
        })


    return jsonify(chat_history)