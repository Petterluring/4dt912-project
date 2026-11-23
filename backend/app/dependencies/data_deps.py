"""Dependencies for accessing data within the FastAPI application."""

from typing import Annotated, cast

from fastapi import Depends, Request
from pandas import DataFrame


def get_data(request: Request) -> DataFrame:
    """Retrieve the data stored in the FastAPI application's state."""
    return cast(DataFrame, request.app.state.dataset)

DataDependency = Annotated[DataFrame, Depends(get_data)]
