from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from pathlib import Path
from models.chat_model import ChatMessage
import os
from config import Config
from extensions import db,bcrypt,jwt

from routes.auth_routes import auth_bp
from routes.chat_routes import chat_bp
from routes.booking_routes import booking_bp
from routes.payment_routes import payment_bp

from models.user_model import User
from models.hotel_model import Hotel
from models.booking_model import Booking
from models.payment_model import Payment

env_path = (
    Path(__file__).resolve().parent / ".env"
)

load_dotenv(dotenv_path=env_path)

print("API KEY:",os.getenv("OPENAI_API_KEY"))

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)

db.init_app(app)
bcrypt.init_app(app)
jwt.init_app(app)

app.register_blueprint(auth_bp)
app.register_blueprint(chat_bp)
app.register_blueprint(booking_bp)
app.register_blueprint(payment_bp)

@app.route("/")
def home():

    return {
        "message": "AI Tourism Backend Running"
    }


with app.app_context():

    db.create_all()

if __name__ == "__main__":

    app.run(debug=True)