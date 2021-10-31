from apps.interfaces import *


class MyValidator(FlaskForm):
    name = StringField("name", validators=[DataRequired()])
    age = IntegerField("age", validators=[DataRequired()])
    email = StringField("email")
