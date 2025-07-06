import sqlite3
import os

from database0607.database import DATABASE_NAME, Session
import create_database as db_creator

from database0607.people import People

# from sqlalchemy import and_, or_, not_, desc, func, distinct

if __name__ == '__main__':
    db_is_creator = os.path.exists(DATABASE_NAME)
    if not db_is_creator:
        db_creator.create_database()

    session = Session()