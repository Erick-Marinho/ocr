from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class OcrResultBase(BaseModel):
    filename: str
    extracted_text: Optional[str] = None

class OcrResultCreate(OcrResultBase):
    pass

class OcrResultResponse(OcrResultBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
        

