from abc import ABC, abstractmethod
from .models import OcrResult

class IOcrResultRepository(ABC):
    @abstractmethod
    def save(self, ocr_result: OcrResult) -> OcrResult:
        pass

    @abstractmethod
    def find_by_id(self, result_id: int) -> OcrResult | None:
        pass