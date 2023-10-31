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
    class Meta:
        table_name = "book"


@snapshot.append
class Student(peewee.Model):
    full_name = CharField(max_length=255)
    login = CharField(max_length=255)
    password = CharField(max_length=255)
    class Meta:
        table_name = "student"


