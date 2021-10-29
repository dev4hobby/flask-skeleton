from apps import mongo

user = mongo.db.client.get_database("user")


def get_user_by_token(token: str) -> dict:
    # provider like google, facebook, kakao.. etc..
    result = user.provider.find_one({"token": token}, {"_id": False})
    return result

def get_users_by_email(email: str) -> list:
    result = user.provider.find(
        {"email": {"$regex": f".*{email}.*"}},
        {"_id": False},
    )
    return list(result)

def get_users_by_name_with_email(name: str, email: str) -> list:
    result = user.provider.find(
        {
            "$and": [
                {"name": name},
                {"email": {"$regex": f".*{email}.*"}},
            ]
        },
        {"_id": False},
    )
    return list(result)

