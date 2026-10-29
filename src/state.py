from pydantic import BaseModel

class SummarizerState(BaseModel):
    text: str
    edited_text: str = ""
    result: str = ""