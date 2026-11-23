"""Hello route for the FastAPI application."""

from typing import Any

from fastapi import APIRouter

from app.dependencies import DatasetDependency

router = APIRouter(prefix="/api/hello", tags=["hello"])

@router.get("/")
def hello() -> dict[str, str]:
    """Endpoint returning a hello message."""
    return {"message": "Hello from FastAPI"}


@router.get("/dataset")
def hello_dataset(
    data: DatasetDependency
) -> dict[str, Any]:
    """Endpoint returning a hello message from the dataset that is currently loaded into the application."""
    return {
        "message": "Hello from the dataset",
        "metadata": {
            "dataset_name": data.attrs["dataset_name"],
            "dataset_size": data.shape[0],
            "columns_count": data.shape[1],
            "columns": list(data.columns)
        }
    }
