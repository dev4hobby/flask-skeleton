import json
from email.utils import parseaddr
from flask import Blueprint, request, render_template
from apps.interfaces.wtfLab import MyValidator

wtf = Blueprint("wtf", __name__, url_prefix="/wtf")


@wtf.route("/lab", methods=["GET"])
def render_wtf_lab_page():
    return render_template("wtf-lab.html", form=MyValidator())


@wtf.route("/user", methods=["POST"])
def check_without_wtf():

    body = request.get_json()
    name = str(body.get("name"))
    age = body.get("age")
    email = str(body.get("email"))
    if (not name) or (not age):
        return {"error": "name or age is missing"}, 400
    try:
        age = int(age)
    except ValueError:
        return {"error": "age is not a number"}, 400
    email = parseaddr(email)[1]

    response = {
        "name": name,
        "age": age,
        "email": email,
    }

    return response, 200


@wtf.route("/user-with-wtf", methods=["POST"])
def get_user_with_wtf():
    body = MyValidator(meta={"csrf": False})
    if body.validate():
        return json.dumps(body.data), 200
    return json.dumps(body.errors), 400


@wtf.route("/user-with-wtf", methods=["GET"])
def get_user_query_with_wtf():
    query = MyValidator(request.args, meta={"csrf": False})
    if query.validate():
        return json.dumps(query.data), 200
    return json.dumps(query.errors), 400


@wtf.route("/user-form-with-wtf", methods=["POST"])
def get_user_form_with_wtf():
    form = MyValidator(request.form)
    if form.validate_on_submit():
        return json.dumps(form.data), 200
    return json.dumps(form.errors), 400
