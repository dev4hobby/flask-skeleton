from database import db
from utils.auth import generate_key


def set_user(provider: str, info: dict) -> bool:
    # provider like google, facebook, kakao.. etc..
    auth = generate_key(64)
    result = db.get_collection("user").insert_one(
        {"provider": provider, "auth": auth, **info}
    )
    return auth


def get_user_by_user_id(provider: str, user_id: str) -> dict:
    # provider like google, facebook, kakao.. etc..
    result = db.get_collection("user").find_one({"id": user_id}, {"_id": False})
    return result


def get_user_by_user_auth(auth: str) -> dict:
    result = db.get_collection("user").find_one({"auth": auth}, {"_id": False})
    return result


def get_users_by_email(email: str) -> list:
    result = db.get_collection("user").find(
        {"email": {"$regex": f".*{email}.*"}},
        {"_id": False},
    )
    return list(result)


def get_users_by_name_with_email(name: str, email: str) -> list:
    result = db.get_collection("user").find(
        {
            "$and": [
                {"name": name},
                {"email": {"$regex": f".*{email}.*"}},
            ]
        },
        {"_id": False},
    )
    return list(result)
