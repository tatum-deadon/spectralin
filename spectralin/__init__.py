"""Spectralin -- Static analysis and code quality scanner."""

__version__ = "0.1.0"

from spectralin.scanner import Scanner
from spectralin.rules import RuleSet

__all__ = ["Scanner", "RuleSet"]
