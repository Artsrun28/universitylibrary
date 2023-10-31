from .db import database
from peewee import CharField
from hashlib import sha256
from config import AppConfig


class User(database.Model):
    username = CharField(max_length=50)
    password = CharField()
    full_name = CharField()
    email = CharField(max_length=255)
    role = CharField()


    @classmethod
    def from_registration_form(cls, form):
        return cls(
            username=form.username.data,
            password=cls.hash_password(form.username.data, form.password.data),
            full_name=form.full_name.data,
            email=form.email.data,
            role=form.role.data,
        )


    @staticmethod
    def hash_password(username, password):
        salted_password = f"{AppConfig.SALT_KEY}.{username}:{password}.{AppConfig.SALT_KEY}"
        hash_generator = sha256(salted_password.encode())
        return hash_generator.hexdigest()
