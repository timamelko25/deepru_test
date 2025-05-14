from fastapi import FastAPI
from fastapi.exceptions import HTTPException
import uvicorn

from app.schemas import StatusResponse
from app.router import router as router_pages


app = FastAPI(
    title="Simple App",
    description="Test app for deepru",
    version="0.0.1",
)


@app.get("/healthcheck/", response_model=StatusResponse)
async def healthcheck():
    return StatusResponse(
        status="ok",
        detail="Service healthy",
    )


@app.exception_handler(Exception)
async def custom_exception_handler(request, exc):
    return HTTPException(
        status_code=500,
        content={"detail": "Internal server error"},
    )


app.include_router(router=router_pages)

if __name__ == "__main__":
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8001,
    )
