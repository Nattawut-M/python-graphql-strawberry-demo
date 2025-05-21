import typing

import strawberry
from faker import Faker


# create a Book type with title and author fields from decorator
@strawberry.type
class Book:
    title: str
    content: str
    author: str


# create a Query type with a books field that returns a list of Book objects
@strawberry.type
class Query:
    books: typing.List[Book]


def get_books():
    fake = Faker()

    books = []
    for _ in range(100):
        book = Book(
            title=fake.sentence(),
            content=fake.paragraph(),
            author=fake.name(),
        )
        books.append(book)

    return books


@strawberry.type
class Query:
    books: typing.List[Book] = strawberry.field(resolver=get_books, metadata={"description": "List of books (generated from Faker)"})


schema = strawberry.Schema(query=Query)
