from app.domain.repositories import IOcrResultRepository
from app.domain.models import OcrResult

class OcrService:
    def __init__(self, ocr_repository: IOcrResultRepository):
        self._repository = ocr_repository

    def create_new_ocr_result(self, filename: str, text: str) -> OcrResult:
        if not filename.endswith(".pdf"):
            raise ValueError("Formato de arquivo inválido")
        
        new_result = OcrResult(filename=filename, extracted_text=text)

        return self._repository.save(new_result)