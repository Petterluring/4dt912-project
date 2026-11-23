"""Tests for the router.hello module."""

from collections.abc import Iterator
from pathlib import Path
from random import Random

import pandas as pd
import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from app.router.hello import router


@pytest.fixture
def client(tmp_path: Path) -> Iterator[TestClient]:
    """Create an isolated app with a CSV-backed dataset."""
    random = Random(42)
    csv_path = tmp_path / "sample.csv"
    pd.DataFrame(
        {
            "student_id": [random.randint(100, 999) for _ in range(4)],
            "score": [random.randint(0, 100) for _ in range(4)],
        }
    ).to_csv(csv_path, index=False)
    dataset = pd.read_csv(csv_path)
    dataset.attrs["dataset_name"] = csv_path.name

    app = FastAPI()
    app.include_router(router)
    app.state.dataset = dataset
    with TestClient(app) as test_client:
        yield test_client


def test_hello(client: TestClient) -> None:
    """Return the greeting from the hello endpoint."""
    response = client.get("/api/hello/")

    assert response.status_code == 200
    assert response.json() == {"message": "Hello from FastAPI"}


def test_hello_dataset(client: TestClient) -> None:
    """Return metadata for the dataset stored in app state."""
    response = client.get("/api/hello/dataset")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Hello from the dataset",
        "metadata": {
            "dataset_name": "sample.csv",
            "dataset_size": 4,
            "columns_count": 2,
            "columns": ["student_id", "score"],
        },
    }
