from fastapi import Depends
from sqlalchemy.orm import Session

from app.infrastructure.database.session import get_db_session
from app.infrastructure.database.repositories import SqlAlchemyOcrRepository
from app.application.service import OcrService

def get_ocr_service(db_session: Session = Depends(get_db_session)) -> OcrService:
    """
    Função de dependência que cria e retorna uma instância do OcrService.
    
    Args:
        db_session: Sessão do banco de dados injetada pelo FastAPI
        
    Returns:
        OcrService: Instância do serviço OCR configurada com o repositório
    """
    # 1. Cria a implementação concreta do repositório
    repo = SqlAlchemyOcrRepository(db_session)
    # 2. Cria o serviço, injetando o repositório nele
    return OcrService(ocr_repository=repo) 