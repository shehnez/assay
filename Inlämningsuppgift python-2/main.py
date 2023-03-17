from fastapi import FastAPI, Depends, HTTPException
import models

from database import Base, engine, SessionLocal
from sqlalchemy.orm import Session

Base.metadata.create_all(engine)

def get_session():
    Session = SessionLocal()
    try:
        yield Session
    finally:
        Session.close()    

from pydantic import BaseModel

class Book(BaseModel):
    id: int = None
    title: str
    aurthor: str
    description: str
    rating: int

app = FastAPI()




@app.get("/")
def root():
    return "Hello and welcome to shehnez books!"

@app.get("/")
def get_books(session: Session = Depends(get_session)):
    books = session.query(models.Book).all()
    return "books"

@app.get("/book/{id}")
def get_book(id:int, session: Session = Depends(get_session)):
    book = session.query(models.Book).get(id)
    return "book"

@app.post("/")
def add_book():
    return "book"

@app.post("/add_book")
def add_book(book: Book, session: Session = Depends(get_session)):
    book_model = models.Books()
    book_model.title = book.title
    book_model.author = book.aurthor
    book_model.description = book.description
    book_model.rating = book.rating

    session.add(book_model)
    session.commit()


    return "book"



@app.delete("/delete_book/{id}")
def delete_book(id: int, session: Session = Depends(get_session)):
    book_model = session.query(models.Books).delete(id)
    session.commit()
    return "book"

@app.put("/update_book/ {id}")
def update_book(id: int, session: Session = Depends(get_session)):

    book_model = session.query(models.Books).get(id)
    book_model = models.Books()
    book_model.title = Book.title
    book_model.author = Book.aurthor
    book_model.description = Book.description
    book_model.rating = Book.rating

    session.add(book_model)
    session.commit()
    return "book" 