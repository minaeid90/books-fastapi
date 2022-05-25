
from typing import Optional
from fastapi import FastAPI
from enum import Enum
app = FastAPI()

BOOKS = {
    "book_1": {
        "title": "Title 1",
        "author": "Author 1"
    },
    "book_2": {
        "title": "Title 2",
        "author": "Author 2"
    },
    "book_3": {
        "title": "Title 3",
        "author": "Author 3"
    },
    "book_4": {
        "title": "Title 4",
        "author": "Author 4"
    },
    "book_5": {
        "title": "Title 5",
        "author": "Author 5"
    },
}

# @app.get("/")
# async def home():
#     return {"message":"Hello world"}


@app.get("/")
async def read_books():
    return BOOKS


@app.get("/book/{title}")
async def book_title(title):
    return {"title": title}


@app.get("/book/{id}")
async def book_id(id: int):
    return {'id': id}


class Direction(str, Enum):
    north = 'North'
    south = 'South'
    east = 'East'
    west = 'West'


@app.get('/direction/{direction}')
async def direction(direction: Direction):
    if direction == 'North':
        return {'direction': direction, 'sub': 'up'}
    elif direction == 'South':
        return {'direction': direction, 'sub': 'down'}
    elif direction == 'East':
        return {'direction': direction, 'sub': 'right'}
    elif direction == 'West':
        return {'direction': direction, 'sub': 'left'}


@app.get('/{book_name}')
async def book_name(book_name: str):
    return BOOKS[book_name]


@app.get('/skip/')
async def skip_book(book_name: Optional[str] = None):
    if book_name:
        new_books = BOOKS.copy()
        del new_books[book_name]
        return new_books
    return BOOKS


@app.post('/')
async def create_book(book_title, book_auhor):
    current_book = 0
    if len(BOOKS) > 0:
        for book in BOOKS:
            x = int(book.split('_')[-1])
            if x > current_book:
                current_book = x

    BOOKS[f"book_{current_book+1}"] = {'title': book_title,
                                        'author': book_auhor}
    return BOOKS[f"book_{current_book+1}"]

@app.put('/book/{book_name}')
async def update_book(book_name, book_title,book_author):

    book_info = {'title':book_title, 'author': book_author}
    BOOKS[book_name] = book_info
    return BOOKS[book_name]

@app.delete('/book/{book_name}')
async def delete_book(book_name:str):
    if book_name in BOOKS:
        del BOOKS[book_name]
        return BOOKS 

        