from pydantic import BaseModel


class SessionDTO(BaseModel):
    id: int
    date: str