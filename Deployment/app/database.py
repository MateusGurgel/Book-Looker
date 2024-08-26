import sqlite3

from contextlib import contextmanager

DATABASE_PATH = "database.db"

@contextmanager
def get_db_connection(db_name=DATABASE_PATH):
    conn = sqlite3.connect(db_name)
    try:
        yield conn
    finally:
        conn.close()

@contextmanager
def get_db_cursor(db_name=DATABASE_PATH):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    try:
        yield cursor
    finally:
        conn.commit()
        conn.close()