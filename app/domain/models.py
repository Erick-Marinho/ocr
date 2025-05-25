from pydantic import BaseModel, Field
from datetime import datetime, timezone

class OcrResult(BaseModel):
    id: int | None = None
    filename: str
    extracted_text: str
    created_at: datetime = Field(default_factory=datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=datetime.now(timezone.utc))

    class Config:
        from_attributes = True