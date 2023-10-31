# auto-generated snapshot
from peewee import *
import datetime
import peewee


snapshot = Snapshot()


@snapshot.append
class Book(peewee.Model):
    book_name = CharField(max_length=255)
    author_name = CharField(max_length=255)
    release_year = IntegerField()
    book_copy = IntegerField()
    class Meta:
        table_name = "book"


@snapshot.append
class Student(peewee.Model):
    full_name = CharField(max_length=255)
    login = CharField(max_length=255)
    password = CharField(max_length=255)
    class Meta:
        table_name = "student"


@snapshot.append
class UserModel(peewee.Model):
    username = CharField(max_length=50)
    password = CharField(max_length=255)
    full_name = CharField(max_length=255)
    email = CharField(max_length=255)
    class Meta:
        table_name = "usermodel"


