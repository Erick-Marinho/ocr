from fastapi import FastAPI, Depends, HTTPException
from contextlib import asynccontextmanager

import database
import models
import schemas


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("API inciando - ", app.title)
    yield
    print("API finalizando - ", app.version)

app = FastAPI(
    lifespan=lifespan,
    title="API OCR com FastAPI, PostgreSQL e SQLAlchemy",
    version="1.0.0",
    description="API para processamento OCR com armazenamento em PostgreSQL e migrações de banco de dados gerenciadas pelo Alembic."
)

@app.get("/", summary="Verifica se a API está em execução")
def root_controller():
    return {"status": "API FastAPI (com Alembic) está em execução!"}

