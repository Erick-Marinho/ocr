from fastapi import APIRouter, Depends
from app.application.service import OcrService
from app.presentation.schemas import OcrResultCreate, OcrResultResponse
from app.infrastructure.di.dependencies import get_ocr_service

router = APIRouter()

@router.post("/", response_model=OcrResultResponse, status_code=201)
def create_ocr_result(
    result_data: OcrResultCreate,
    ocr_service: OcrService = Depends(get_ocr_service)
):
    # A responsabilidade do router é apenas passar os dados para a camada de aplicação
    created_result = ocr_service.create_new_ocr_result(
        filename=result_data.filename,
        text=result_data.extracted_text
    )
    return created_result