from pydantic import BaseModel
from datetime import datetime

class OcrResultCreate(BaseModel):
    filename: str
    extracted_text: str

class OcrResultResponse(BaseModel):
    id: int
    filename: str
    extracted_text: str
    created_at: datetime

    class Config:
        from_attributes = True 