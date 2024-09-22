"""CLI entry point."""

import argparse


def main():
    parser = argparse.ArgumentParser(prog="spectralin", description="Code quality scanner")
    sub = parser.add_subparsers(dest="command")

    scan_p = sub.add_parser("scan", help="Scan a directory")
    scan_p.add_argument("path", help="Path to scan")
    scan_p.add_argument("--format", choices=["text", "json"], default="text")
    scan_p.add_argument("--severity", choices=["error", "warn", "info"], default="info")

    sub.add_parser("rules", help="List active rules")

    args = parser.parse_args()

    if args.command == "scan":
        from spectralin import Scanner
        scanner = Scanner()
        report = scanner.scan(args.path)
        if args.format == "json":
            print(report.to_json())
        else:
            report.print()
    elif args.command == "rules":
        from spectralin import RuleSet
        for r in RuleSet.default().rules:
            print(f"  [{r.severity}] {r.name}: {r.message}")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
