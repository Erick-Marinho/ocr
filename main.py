import logging
from fastapi import FastAPI

from app.infrastructure.database.session import engine
from app.infrastructure.database.orm import Base
from app.presentation.routers import router as ocr_router

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Cria as tabelas no banco de dados (se não existirem)
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="OCR API",
    description="API para extração de texto de arquivos",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

app.include_router(ocr_router, prefix="/ocr", tags=["OCR"])

@app.get("/", summary="Verifica se a API está rodando")
def root():
    return {
        "status": "API FastAPI em execução",
        "version": app.version,
        "docs": "/docs"
    }
