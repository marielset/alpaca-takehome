from pydantic import BaseModel

class SessionNoteCreate(BaseModel):
    note: str

class SessionNoteResponse(BaseModel):
    id: int
    note: str

    class Config:
        orm_mode = True