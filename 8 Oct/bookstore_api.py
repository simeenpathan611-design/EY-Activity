from typing import List, Optional
from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel

app = FastAPI()

class Book(BaseModel):
    id:int
    title: str
    author: str
    price: float
    in_stock: bool

books = [
    Book(id=1, title="Deep Learning", author="Ian GoodFellow", price=1200, in_stock=True),
    Book(id=2,title="Python Tricks",author="Dan Bader",price=7000,in_stock=False),
    Book(id=3,title="Clean Code",author="Robert C.Martin",price=850,in_stock=True),
    ]

@app.get("/books",response_model=List[Book])
def get_all_books():
    return books

@app.get("/books{/book_id})",response_model=List[Book])
def get_books(book_id: int):
    for book in books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@app.post("/books/{book_id}",response_model=Book)
def add_book(new_book: Book):
    for book in books:
        if book.id == new_book.id:
            raise HTTPException(status_code=400, detail="Book already exists")
        books.append(new_book)
        return new_book

@app.put("/books/{book_id}",response_model=Book)
def update_book(book_id: int, updated_book: Book):
    for i,book in enumerate(books):
        if book.id == book_id:
            books[i] = updated_book.dict()
            return updated_book
    raise HTTPException(status_code=404, detail="Book not found")

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for i,book in enumerate(books):
        if book.id == book_id:
            books.remove(book)
            return {"message":"book deleted"}
    raise HTTPException(status_code=404, detail="Book not found")

@app.get("/books/search",response_model=List[Book])
def search_books(author:Optional[str]=Query(None),max_price:Optional[float]=Query(None)):
    results = books
    if author:
        results = [book for book in results if book.author == author]
    if max_price is not None:
        results = [book for book in results if book.price > max_price]

    if not results:
        raise HTTPException(status_code=404, detail="Book not found")

    return results

@app.get("/books/available",response_model=List[Book])
def available_books():
    available = [books for books in books if books.in_stock]
    return available

@app.get("/books/count")
def count_books():
    return{"total_books":len(books)}