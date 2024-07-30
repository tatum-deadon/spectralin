"""The main scanning engine."""

from __future__ import annotations
from typing import List, Dict, Optional, Any
from spectralin.rules import RuleSet
from spectralin.report import Report, Issue
import os
import time


class Scanner:
    """Static analysis scanner.

    Scans source files against a set of rules and produces
    a report of issues found.

    Example:
        >>> scanner = Scanner()
        >>> report = scanner.scan("./src")
        >>> print(report.summary())
    """

    def __init__(self, rules: Optional[RuleSet] = None, config: Optional[Dict] = None):
        self.rules = rules or RuleSet.default()
        self.config = config or {}
        self._file_count = 0
        self._line_count = 0

    def scan(self, path: str) -> Report:
        """Scan a file or directory."""
        start = time.perf_counter()
        issues: List[Issue] = []

        if os.path.isfile(path):
            issues.extend(self._scan_file(path))
        elif os.path.isdir(path):
            for root, dirs, files in os.walk(path):
                dirs[:] = [d for d in dirs if d not in {".git", "node_modules", "__pycache__", ".venv"}]
                for f in files:
                    if f.endswith((".py", ".js", ".ts", ".rs", ".go")):
                        fp = os.path.join(root, f)
                        issues.extend(self._scan_file(fp))

        elapsed = time.perf_counter() - start
        return Report(issues, self._file_count, self._line_count, elapsed)

    def _scan_file(self, path: str) -> List[Issue]:
        """Scan a single file."""
        issues = []
        try:
            with open(path) as f:
                lines = f.readlines()
            self._file_count += 1
            self._line_count += len(lines)
            for i, line in enumerate(lines, 1):
                for rule in self.rules.active_rules:
                    if rule.matches(line, path, i):
                        issues.append(Issue(
                            severity=rule.severity,
                            message=rule.message,
                            file=path,
                            line=i,
                            rule=rule.name,
                        ))
        except Exception:
            pass
        return issues
