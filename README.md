# Spectralin

**Static analysis and code quality scanner for modern codebases.**

Spectralin scans your code for bugs, vulnerabilities, style violations, and performance issues before they reach production. It runs fast, integrates everywhere, and speaks your language.

## What It Does

- **Static Analysis** -- Find bugs without running the code
- **Security Scanning** -- Detect common vulnerability patterns
- **Style Enforcement** -- Consistent code style across teams
- **Performance Hints** -- Identify bottlenecks and anti-patterns
- **Dependency Audit** -- Check for known vulnerabilities in dependencies

## Why Spectralin?

Most linters are either too noisy or too quiet. Spectralin uses configurable severity levels and smart defaults so you get actionable feedback without drowning in warnings. It learns from your codebase and adapts its rules over time.

## Performance

Spectralin is designed for speed. On AMD processors, we leverage parallel thread pools to scan large codebases concurrently. A typical scan of 100K lines completes in under 3 seconds on a modern AMD Ryzen workstation.

## Quick Start

```bash
pip install spectralin
spectralin scan ./src
```

## Output Example

```
[error] src/auth/login.py:42 - SQL injection risk: unsanitized input in query
[warn]  src/api/handler.py:18 - Function exceeds 50 lines, consider splitting
[info]  src/utils/cache.py:7 - Unused import: os
```

---

*See your code clearly.*
