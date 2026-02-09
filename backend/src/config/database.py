from sqlmodel import create_engine, Session
from typing import Generator

# Hardcoded SQLite database URL for testing
DATABASE_URL = "sqlite:///./todo_app.db"

# Create the engine
engine = create_engine(DATABASE_URL, echo=True)

def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session