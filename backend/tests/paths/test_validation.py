"""Tests for the validate_path function in app.paths.validation."""
from pathlib import Path

import pytest

from app.paths.validation import validate_path


def test_validate_path_accepts_existing_file_as_path(tmp_path: Path) -> None:
    """Test that validate_path accepts an existing file as a Path object."""
    file_path = tmp_path / "file.txt"
    file_path.touch()

    assert validate_path(file_path) is None


def test_validate_path_accepts_existing_file_as_string(tmp_path: Path) -> None:
    """Test that validate_path accepts an existing file as a string path."""
    file_path = tmp_path / "file.txt"
    file_path.touch()

    assert validate_path(str(file_path)) is None


def test_validate_path_accepts_existing_directory(tmp_path: Path) -> None:
    """Test that validate_path accepts an existing directory."""
    assert validate_path(tmp_path, isFile=False) is None


def test_validate_path_raises_for_missing_path(tmp_path: Path) -> None:
    """Test that validate_path raises a FileNotFoundError for a missing path."""
    missing_path = tmp_path / "missing"

    with pytest.raises(FileNotFoundError, match="Path does not exist"):
        validate_path(missing_path)


def test_validate_path_raises_when_file_is_expected_but_directory_given(
    tmp_path: Path,
) -> None:
    """Test that validate_path raises a ValueError when a file is expected but a directory is given."""
    with pytest.raises(ValueError, match="Expected a file"):
        validate_path(tmp_path)


def test_validate_path_raises_when_directory_is_expected_but_file_given(
    tmp_path: Path,
) -> None:
    """Test that validate_path raises a ValueError when a directory is expected but a file is given."""
    file_path = tmp_path / "file.txt"
    file_path.touch()

    with pytest.raises(ValueError, match="Expected a directory"):
        validate_path(file_path, isFile=False)
