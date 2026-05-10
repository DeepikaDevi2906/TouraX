from flask import Blueprint, request, jsonify

from services.auth_service import register_user,login_user

auth_bp = Blueprint("auth_bp", __name__)


@auth_bp.route("/register", methods=["POST"])
def register():

    data = request.json

    name = data.get("name")

    email = data.get("email")

    password = data.get("password")

    result = register_user(
        name=name,
        email=email,
        password=password
    )

    if result["success"]:

        return jsonify(result), 201

    return jsonify(result), 400


@auth_bp.route("/login", methods=["POST"])
def login():

    data = request.json

    email = data.get("email")

    password = data.get("password")

    result = login_user(
        email=email,
        password=password
    )

    if result["success"]:

        return jsonify(result), 200

    return jsonify(result), 401