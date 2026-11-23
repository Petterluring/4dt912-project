"""Tests for the load_csv_file function in app.paths.loading."""
from pathlib import Path

import pandas as pd
import pytest

from app.paths.loading import load_csv_file


def test_load_csv_file_reads_csv_from_path(tmp_path: Path) -> None:
    """Test that load_csv_file correctly reads a CSV file from a given path."""
    csv_path = tmp_path / "data.csv"
    csv_path.write_text("name,value\nAda,42\nGrace,7\n", encoding="utf-8")

    result = load_csv_file(csv_path)

    expected = pd.DataFrame({"name": ["Ada", "Grace"], "value": [42, 7]})
    pd.testing.assert_frame_equal(result, expected)


def test_load_csv_file_accepts_string_path(tmp_path: Path) -> None:
    """Test that load_csv_file correctly reads a CSV file when given a string path."""
    csv_path = tmp_path / "data.csv"
    csv_path.write_text("value\n1\n2\n", encoding="utf-8")

    result = load_csv_file(str(csv_path))

    pd.testing.assert_frame_equal(result, pd.DataFrame({"value": [1, 2]}))


def test_load_csv_file_raises_for_missing_path(tmp_path: Path) -> None:
    """Test that load_csv_file raises a FileNotFoundError for a missing path."""
    csv_path = tmp_path / "missing.csv"

    with pytest.raises(FileNotFoundError, match="Path does not exist"):
        load_csv_file(csv_path)


def test_load_csv_file_raises_for_directory(tmp_path: Path) -> None:
    """Test that load_csv_file raises a ValueError when given a directory path."""
    with pytest.raises(ValueError, match="Expected a file"):
        load_csv_file(tmp_path)
