from fastapi import FastAPI

app = FastAPI(
    title="Minha API Modular com APIRouter",
    version="1.1.0",
    description="Demonstração do uso de APIRouter para organizar endpoints."
)

@app.get("/", summary="Check if the API is running", description="This endpoint is used to check if the API is running.")
def root_controller():
    return {"status": "FastAPI is running"}

