from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, EmailField
from wtforms.validators import InputRequired, EqualTo


class CreateBookForm(FlaskForm):
    book_name = StringField(
        validators=[
            InputRequired(),
        ],
    )

    author_name = StringField(
        validators=[
            InputRequired(),
        ],
    )

    release_year = IntegerField(
        validators=[
            InputRequired(),
        ],
    )

    book_copy = IntegerField(
        validators=[
            InputRequired(),
        ],
    )


class LoginForm(FlaskForm):
    username = StringField(
        validators=[
            InputRequired(),
        ],
    )

    password = StringField(
        validators=[
            InputRequired(),
        ],
    )


class RegisterForm(FlaskForm):
    username = StringField(
        validators=[
            InputRequired(),
        ],
    )

    password = StringField(
        validators=[
            InputRequired(),
        ],
    )

    repeat_password = StringField(
        validators=[
            EqualTo(
                fieldname='password',
                message="Passwords don't match",
            ),
        ],
    )

    full_name = StringField(
        validators=[
            InputRequired(),
        ]
    )

    email = EmailField(
        validators=[
            InputRequired(),
        ]
    )

    role = EmailField(
        validators=[
            InputRequired(),
        ]
    )
