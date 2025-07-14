from fastapi import APIRouter, Depends, Form
from sqlalchemy.orm import Session
from db import SessionLocal
from crud.session_note import create_note
from schemas.session_note import SessionNoteResponse

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/save-note", response_model=SessionNoteResponse)
def save_note(note: str = Form(...), db: Session = Depends(get_db)):
    return create_note(db, note_in={"note": note})