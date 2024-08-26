
from database import get_db_cursor
from datetime import date

class BookLogRepository():
    @staticmethod
    def create_book(price: int, date: date, book_id) -> None:
        with get_db_cursor() as cursor:
            cursor.execute("INSERT INTO book_logs (price, date, book_id) VALUES (?, ?, ?)", (price, date, book_id))
