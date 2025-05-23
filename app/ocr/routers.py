from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_ocr_status():
    return {"status": "OCR API is running"}