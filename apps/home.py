import json
from flask import Blueprint, render_template, url_for, session, request, redirect

home = Blueprint("home", __name__, url_prefix="/")


@home.route("/")
def get_home():
    """
    메인 화면
    """
    from database.user import get_user_by_user_auth

    if "auth" in session:
        user = get_user_by_user_auth(auth=session["auth"])
        return render_template("home.html", hello="Greeting", user=user)
    return render_template(
        "home.html",
        hello="How'bout login?",
    )


@home.route("/login")
def get_login():
    from apps import google

    if session.get("auth"):
        return redirect(url_for("home.get_home"))
    return google.authorize(callback=url_for("home.callback", _external=True))


@home.route("/logout")
def get_logout():
    session.pop("google_token", None)
    return redirect(url_for("home.get_home"))


@home.route("/login/callback")
def callback():
    from apps import google
    from database.user import set_user, get_user_by_user_id

    @google.tokengetter
    def get_google_oauth_token():
        return session.get("google_token")

    resp = google.authorized_response()
    if resp is None:
        return "Access denied: reason=%s error=%s" % (
            request.args["error"],
            request.args["error_description"],
        )
    session["google_token"] = (resp["access_token"], "")
    me = google.get("userinfo")
    user = get_user_by_user_id(provider="google", user_id=me.data.get("id"))
    if not user:
        auth = set_user(provider="google", info=me.data)
        session["auth"] = auth
    else:
        session["auth"] = user.get("auth")
    return redirect(url_for("home.get_home"))
