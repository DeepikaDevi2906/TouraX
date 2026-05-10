from extensions import db

class ChatMessage(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    user_id = db.Column(
        db.Integer,
        nullable=False
    )

    sender = db.Column(
        db.String(20),
        nullable=False
    )

    message = db.Column(
        db.Text,
        nullable=False
    )

    timestamp = db.Column(
        db.DateTime,

        server_default=db.func.now()
    )