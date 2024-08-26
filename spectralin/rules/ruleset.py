"""Rule set management."""

from __future__ import annotations
from typing import List, Optional
from spectralin.rules.rule import Rule


class RuleSet:
    """Collection of rules for scanning."""

    def __init__(self, rules: Optional[List[Rule]] = None):
        self.rules: List[Rule] = rules or []

    @classmethod
    def default(cls) -> "RuleSet":
        """Create a default rule set with common checks."""
        return cls([
            Rule("sql-injection", r"(execute|query)\(.*\+.*\)", "error",
                 "Possible SQL injection: unsanitized input in query"),
            Rule("hardcoded-password", r"password\s*=\s*["\'][^"\']+["\']", "error",
                 "Hardcoded password detected"),
            Rule("unused-import", r"^import\s+\w+$", "info",
                 "Potentially unused import"),
            Rule("long-function", r"^\s*def\s+\w+", "warn",
                 "Function definition (check length)", ["py"]),
            Rule("todo-fixme", r"(TODO|FIXME|HACK|XXX):", "info",
                 "Unresolved TODO/FIXME comment"),
            Rule("eval-usage", r"\beval\s*\(", "warn",
                 "Use of eval() is discouraged"),
            Rule("empty-except", r"except.*:", "warn",
                 "Bare except clause"),
        ])

    @property
    def active_rules(self) -> List[Rule]:
        return [r for r in self.rules if r._enabled]

    def add(self, rule: Rule) -> None:
        self.rules.append(rule)

    def remove(self, name: str) -> None:
        self.rules = [r for r in self.rules if r.name != name]

    def enable_all(self) -> None:
        for r in self.rules:
            r.enable()

    def disable_all(self) -> None:
        for r in self.rules:
            r.disable()
