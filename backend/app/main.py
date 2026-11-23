"""Main entry point for the FastAPI application."""
from contextlib import asynccontextmanager
from logging import getLogger
from typing import AsyncGenerator

from fastapi import FastAPI

from app.paths.constants import DATA_DIR
from app.paths.loading import load_csv_file
from app.router import hello

logger = getLogger("uvicorn.error")

# Test comment
@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    """Manage the lifespan of the FastAPI application."""
    logger.info("Starting FastAPI application lifespan management.")

    csv_file_name = "raw_student_dropout_dataset.csv"
    csv_file_path = DATA_DIR / csv_file_name
    try:
        df = load_csv_file(csv_file_path)
        df.attrs["dataset_name"] = csv_file_name
        app.state.dataset = df
        logger.info(f"CSV file loaded successfully: {csv_file_path}")
    except FileNotFoundError as e:
        logger.error(e)
        raise SystemExit(1)
    except ValueError as e:
        logger.error(e)
        raise SystemExit(1)

    yield
    # Perform any shutdown actions here
    logger.info("Shutting down FastAPI application lifespan management.")

app = FastAPI(lifespan=lifespan)
app.include_router(hello.router)

@app.get("/")
def read_root() -> dict[str, str]:
    """Root endpoint returning a welcome message."""
    return {"message": "Welcome to 4DT912 Backend"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
