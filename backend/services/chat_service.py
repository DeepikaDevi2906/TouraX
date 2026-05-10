from models.chat_model import ChatMessage

from extensions import db

def save_message(user_id,sender,message):

    chat = ChatMessage(

        user_id=user_id,

        sender=sender,

        message=message
    )

    db.session.add(chat)

    db.session.commit()

    return chat


def get_user_messages(user_id):

    messages = ChatMessage.query.filter_by(
        user_id=user_id
    ).all()

    return messages