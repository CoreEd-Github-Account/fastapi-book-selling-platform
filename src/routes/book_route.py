# src\routes\book_route.py
from fastapi import APIRouter
from src.model.book_table import Book
from src.model.user_table import User
from src.service.auth import verify_api_key
from src.utils.api_response import BookResponse
from fastapi.params import Depends
from sqlmodel import Session
from src.db.engine import get_session
from src.validator.user_validation import CreateUserRequest
from src.validator.book_validation import CreateBookRequest



router = APIRouter(
    prefix="/book",
    tags=["book"],
)


# localhost:8000/book
@router.post("/", response_model=BookResponse)
async def create_book(book_data: CreateBookRequest, session: Session = Depends(get_session), api_key: str = Depends(verify_api_key)):
    """create a book into database"""

    book = Book(
        title =   book_data.title,
        author = book_data.author,
        price = book_data.price,
        is_sold = book_data.is_sold,
        user_id = book_data.user_id
    )

    # add user to database
    session.add(book)
    session.commit()
    session.refresh(book)

    return BookResponse(status="success", message="Book has been created", book=[book])


# localhost:8000/book/search
# @router.get("/search", response_model=BookResponse)