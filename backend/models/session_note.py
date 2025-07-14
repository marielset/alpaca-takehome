from sqlalchemy import Column, Integer, String
from db import Base

class SessionNote(Base):
    __tablename__ = "session_notes"
    id = Column(Integer, primary_key=True, index=True)
    note = Column(String)