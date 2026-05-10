from flask_jwt_extended import create_access_token
from extensions import db,bcrypt
from models.user_model import User

def register_user(name,email,password):

    existing_user = User.query.filter_by(
        email=email
    ).first()


    if existing_user:

        return {

            "success": False,

            "message":
                "Email already exists"
        }


    hashed_password = (
        bcrypt
        .generate_password_hash(password)
        .decode("utf-8")
    )


    new_user = User(

        name=name,

        email=email,

        password=hashed_password
    )


    db.session.add(new_user)

    db.session.commit()


    return {

        "success": True,

        "message":
            "User registered successfully"
    }

def login_user(
    email,
    password
):

    user = User.query.filter_by(
        email=email
    ).first()


    if not user:

        return {

            "success": False,

            "message":
                "User not found"
        }


    password_match = (
        bcrypt.check_password_hash(
            user.password,
            password
        )
    )


    if not password_match:

        return {

            "success": False,

            "message":
                "Invalid password"
        }

    access_token = create_access_token(

        identity=str(user.id)
    )


    return {

        "success": True,

        "message":
            "Login successful",

        "token": access_token,

        "user_id": user.id,

        "name": user.name
    }