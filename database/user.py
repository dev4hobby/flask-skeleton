from typing import Union
from database.interfaces.User import User
from utils.auth import generate_key


def set_user(provider: str, info: dict) -> bool:
    # provider like google, facebook, kakao.. etc..
    auth = generate_key(64)
    user = User(
        provider=provider,
        auth=auth,
        _id=info["id"],
        email=info["email"],
        verified_email=info["verified_email"],
        picture=info["picture"],
    )
    user.save()
    return auth


def get_user_by_user_id(provider: str, user_id: str) -> Union[dict, None]:
    try:
        result = User.objects.get(provider=provider, _id=user_id)
        return result
    except User.DoesNotExist:
        return None


def get_user_by_user_auth(auth: str) -> Union[dict, None]:
    try:
        result = User.objects.get(auth=auth)
        return result
    except User.DoesNotExist:
        return None


def get_users_by_email(email: str) -> list:
    result = User.objects(email__regex=f".*{email}.*")
    return result


def get_users_by_name_with_email(name: str, email: str) -> list:
    result = User.objects(name=name, email__regex=f".*{email}.*")
    return result
