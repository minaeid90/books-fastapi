from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel, Field
from uuid import UUID


app = FastAPI()


class Book(BaseModel):
    id: UUID
    title: str = Field(min_length=1)
    author: str = Field(min_length=1,
                        max_length=100)
    description: Optional[str] = Field(title='Description of the book',
                                       min_length=1,
                                       max_length=100)
    rating: int = Field(lt=101, gt=-1)

    class Config:
        schema_extra = {
            "example": {
                "id": "sjkjdf",
                "title": "Hello",
                "author": "Mina",
                "description": "a lot fo descritpion",
                "rating": 17

            }
        }


BOOKS = []


@app.get('/')
async def read_all_books():
    if len(BOOKS) < 1:
        create_books_no_api()
    return BOOKS


@app.get('/book/{book_id}/')
async def get_book(book_id: UUID):
    for i, book in enumerate(BOOKS):
        if book.id == book_id:
            return BOOKS[i]


@app.put('/books/{book_id}/')
async def update_book(book_id: UUID, book: Book):
    for i, book in enumerate(BOOKS):
        if book.id == book_id:
            BOOKS[i] = book
            return BOOKS[i]

@app.delete('/book/{book_id}/')
async def delete_book(book_id:UUID):
    for i, book in enumerate(BOOKS):
        if book.id == book_id:
            del BOOKS[i]
            return '1'


@app.post('/')
async def create_book(book: Book):
    BOOKS.append(book)
    return book


def create_books_no_api():
    book_1 = Book(id="663adb09-8ac3-461c-aa24-a44c5bd50682",
                  author='Author 1', title='Title 1', description='Descritipion 1', rating=60)
    book_2 = Book(id="663aadf9-8ac3-461c-aa24-a44c5bd50682",
                  author='Author 2', title='Title 2', description='Descritipion 2', rating=30)
    BOOKS.append(book_1)
    BOOKS.append(book_2)
