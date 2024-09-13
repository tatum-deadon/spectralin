"""Scan report generation."""

from __future__ import annotations
from typing import List, Dict
from dataclasses import dataclass
import json


@dataclass
class Issue:
    """A single issue found during scanning."""
    severity: str
    message: str
    file: str
    line: int
    rule: str

    def format(self, color: bool = True) -> str:
        prefix = {"error": "\033[91m[error]\033[0m",
                  "warn": "\033[93m[warn]\033[0m",
                  "info": "\033[94m[info]\033[0m"}
        p = prefix.get(self.severity, f"[{self.severity}]")
        if not color:
            p = f"[{self.severity}]"
        return f"{p} {self.file}:{self.line} - {self.message}"


class Report:
    """Aggregated scan report."""

    def __init__(self, issues: List[Issue], files: int, lines: int, elapsed: float):
        self.issues = issues
        self.files = files
        self.lines = lines
        self.elapsed = elapsed

    @property
    def errors(self) -> List[Issue]:
        return [i for i in self.issues if i.severity == "error"]

    @property
    def warnings(self) -> List[Issue]:
        return [i for i in self.issues if i.severity == "warn"]

    def summary(self) -> str:
        return (
            f"Scanned {self.files} files ({self.lines} lines) in {self.elapsed:.2f}s\n"
            f"  Errors: {len(self.errors)}\n"
            f"  Warnings: {len(self.warnings)}\n"
            f"  Total: {len(self.issues)}"
        )

    def print(self, color: bool = True) -> None:
        for issue in sorted(self.issues, key=lambda i: (i.file, i.line)):
            print(issue.format(color))
        print()
        print(self.summary())

    def to_json(self) -> str:
        return json.dumps([
            {"severity": i.severity, "file": i.file, "line": i.line,
             "message": i.message, "rule": i.rule}
            for i in self.issues
        ], indent=2)
