"""Individual rule definition."""

from __future__ import annotations
from typing import Optional
import re


class Rule:
    """A single analysis rule.

    Each rule defines a pattern to match, severity level,
    and an explanatory message.
    """

    def __init__(self, name: str, pattern: str, severity: str = "warn",
                 message: str = "", languages: Optional[list] = None):
        self.name = name
        self.pattern = re.compile(pattern, re.IGNORECASE)
        self.severity = severity
        self.message = message or f"Rule {name} violation"
        self.languages = languages or ["*"]
        self._enabled = True

    def matches(self, line: str, filepath: str, line_num: int) -> bool:
        """Check if a line matches this rule."""
        if not self._enabled:
            return False
        ext = filepath.rsplit(".", 1)[-1] if "." in filepath else ""
        if "*" not in self.languages and ext not in self.languages:
            return False
        return bool(self.pattern.search(line))

    def disable(self) -> None:
        self._enabled = False

    def enable(self) -> None:
        self._enabled = True

    def __repr__(self) -> str:
        return f"Rule({self.name}, {self.severity})"
