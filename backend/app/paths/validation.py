"""Validation functions for file system paths."""

from pathlib import Path


def validate_path(path: Path | str, isFile: bool = True) -> None:
    """Validate that the given path exists and is a file or directory.

    Args:
        path (Path | str): The path to validate.
        isFile (bool, optional): Whether the path should be a file. Defaults to True.

    Raises:
        FileNotFoundError: If the path does not exist.
        ValueError: If the path is not of the expected type (file or directory).

    """
    if isinstance(path, str):
        path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"Path does not exist: {path}")
    if isFile and not path.is_file():
        raise ValueError(f"Expected a file, but got: {path}")
    if not isFile and not path.is_dir():
        raise ValueError(f"Expected a directory, but got: {path}")
