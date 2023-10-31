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


def forward(old_orm, new_orm):
    book = new_orm['book']
    return [
        # Apply default value 0 to the field book.book_copy,
        book.update({book.book_copy: 0}).where(book.book_copy.is_null(True)),
    ]
