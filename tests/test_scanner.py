"""Tests for Scanner."""

import pytest
import tempfile
import os
from spectralin import Scanner


def test_scan_python_file():
    with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False) as f:
        f.write("password = \"secret123\"\n")
        f.flush()
        scanner = Scanner()
        report = scanner.scan(f.name)
        assert len(report.issues) > 0
        os.unlink(f.name)


def test_scan_empty_file():
    with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False) as f:
        f.write("# clean file\n")
        f.flush()
        scanner = Scanner()
        report = scanner.scan(f.name)
        assert len(report.errors) == 0
        os.unlink(f.name)
