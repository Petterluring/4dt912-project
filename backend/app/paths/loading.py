"""Module for file loading functions."""

from pathlib import Path

from pandas import DataFrame, read_csv

from .validation import validate_path


def load_csv_file(path: Path | str) -> DataFrame:
    """Load a CSV file into a DataFrame.

    Args:
        path (Path | str): The path to the CSV file.

    Returns:
        DataFrame: The loaded CSV data.

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If the path is not a file.

    """
    if isinstance(path, str):
        path = Path(path)
    validate_path(path, isFile=True)
    return read_csv(path)
