from fastapi import FastAPI,Depends,HTTPException
from Services.services import get_books,create_book,get_book,update_book,delete_book
import models,schemas

from db import get_db,engine
from sqlalchemy.orm import Session


app = FastAPI()

@app.get("/books/", response_model=list[schemas.Book])
def get_all_books(db:Session = Depends(get_db)):
    return get_books(db)

@app.post("/books/", response_model=schemas.Book)
def create_new_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    return create_book(db, book)

@app.get("/books/{id}",response_model=schemas.Book)
def get_book_by_id(id: int, db: Session = Depends(get_db)):
    book_queryset = get_book(db, id)
    if not book_queryset:
        raise HTTPException(status_code=404, detail="Invalid Book ID")
    return book_queryset

@app.put("/books/{id}",response_model=schemas.Book)
def Update_book(book: schemas.BookCreate, id: int, db:Session = Depends(get_db)):
                 db_update = update_book(db, book, id)
                 if not db_update:
                    raise HTTPException(status_code=404, detail="Book not found")
                 return db_update

@app.delete("/books/{id}",response_model=schemas.Book)
def Delete_book(id: int, db:Session = Depends(get_db)):
      delete_entry = delete_book(db, id)
      if not delete_entry:
        raise HTTPException(status_code=404, detail="Book not found")
      return delete_entry

