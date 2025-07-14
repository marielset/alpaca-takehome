from sqlalchemy.orm import Session
from models.session_note import SessionNote
from schemas.session_note import SessionNoteCreate

def create_note(db: Session, note_in: SessionNoteCreate) -> SessionNote:
    note = SessionNote(note=note_in['note'])
    db.add(note)
    db.commit()
    db.refresh(note)
    return note