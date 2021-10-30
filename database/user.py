from apps import mongo
from utils.auth import generate_key
from settings import DATABASES

user = mongo.db.client.get_database(DATABASES.get("name"))

"""
1. 클라에서 access_token, provider, social_id 들고와
2. provider에 access_token을 던져서 social_id랑 유저정보가 같은지 확인
3. 있으면 유저 정보 세션에 넣고 로그인 성공
4. 없으면 회원가입 페이지로 이동
"""


def set_user(provider: str, info: dict) -> bool:
    # provider like google, facebook, kakao.. etc..
    auth = generate_key(64)
    result = user.get_collection("user").insert_one(
        {"provider": provider, "auth": auth, **info}
    )
    return auth


def get_user_by_user_id(provider: str, user_id: str) -> dict:
    # provider like google, facebook, kakao.. etc..
    result = user.get_collection("user").find_one({"id": user_id}, {"_id": False})
    return result


def get_user_by_user_auth(auth: str) -> dict:
    result = user.get_collection("user").find_one({"auth": auth}, {"_id": False})
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
