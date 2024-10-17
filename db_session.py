from db_postgres.session import SessionLocal
from db_cloudant.session import CloudantSessionLocal
from typing import Generator

def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

def get_cdb() -> Generator:
    try:
        cdb = CloudantSessionLocal
        yield cdb

    finally:
        print("cloudant session closed")
        # cdb.close()