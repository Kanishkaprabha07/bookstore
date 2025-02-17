from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from app import crud, models, schemas, database

app = FastAPI()

# Create the tables in the database
@app.on_event("startup")
async def startup():
    async with database.engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)

# Get all books (with pagination)
@app.get("/books/", response_model=list[schemas.BookResponse])
async def list_books(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    books = crud.list_books(db, skip=skip, limit=limit)
    return books

# Create a new book
@app.post("/books/", response_model=schemas.BookResponse)
async def create_book(book: schemas.BookCreate, db: Session = Depends(database.get_db)):
    db_book = crud.create_book(db, book)
    return db_book

# Get a book by ID
@app.get("/books/{book_id}", response_model=schemas.BookResponse)
async def get_book(book_id: int, db: Session = Depends(database.get_db)):
    db_book = crud.get_book(db, book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

# Update a book by ID
@app.put("/books/{book_id}", response_model=schemas.BookResponse)
async def update_book(book_id: int, book: schemas.BookCreate, db: Session = Depends(database.get_db)):
    db_book = crud.update_book(db, book_id, book)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

# Delete a book by ID
@app.delete("/books/{book_id}")
async def delete_book(book_id: int, db: Session = Depends(database.get_db)):
    db_book = crud.delete_book(db, book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"message": "Book deleted successfully"}
