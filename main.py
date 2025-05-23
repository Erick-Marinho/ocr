import logging
# import ocr.models as models
# import ocr.schemas as schemas

from fastapi import FastAPI, Depends, HTTPException, status
from ocr import routers as ocr_routers
from datetime import datetime
from app.database import SessionLocal, get_db
from contextlib import asynccontextmanager
from sqlalchemy.orm import Session
from sqlalchemy import text

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info(f"API iniciando - {app.title} v{app.version}")

    try:
        db = SessionLocal()
        db.execute(text("SELECT 1"))
        db.close()
        logger.info("Conexão com o banco de dados estabelecida com sucesso")
    except Exception as e:
        logger.error(f"Erro ao conectar ao banco de dados: {e}")
        raise

    yield

    logger.info(f"API finalizando - {app.title} v{app.version}")

app = FastAPI(
    lifespan=lifespan,
    title="API OCR com FastAPI, PostgreSQL e SQLAlchemy",
    version="1.0.0",
    description="API para processamento OCR com armazenamento em PostgreSQL e migrações de banco de dados gerenciadas pelo Alembic.",
    docs_url="/docs",
    redoc_url="/redoc"
)

app.include_router(ocr_routers.router, prefix="/ocr", tags=["OCR"])

@app.get("/", summary="Verifica se a API está em execução")
def root_controller():
    return {
        "status": "API FastAPI está em execução!",
        "version": app.version,
        "docs": "/docs",
    }

@app.get("/health", summary="Health check da aplicação")
def health_check(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
        return {
            "status": "healthy",
            "database": "connected",
            "timestamp": datetime.now().isoformat()
        }
    except Exception as e:
        logger.error(f"Health check falhou: {e}")
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE, 
            detail="Database connection failed"
        )