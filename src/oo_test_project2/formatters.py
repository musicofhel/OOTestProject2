"""Output formatters for reports."""


def format_text(report: dict) -> str:
    """Format a summary report as plain text."""
    lines = [
        "=== User Summary Report ===",
        f"Total users: {report['total']}",
        f"Active: {report['active']}",
        f"Inactive: {report['inactive']}",
        f"Active rate: {report['active_rate']:.0%}",
        "",
        "Roles:",
    ]
    for role, count in sorted(report.get("roles", {}).items()):
        lines.append(f"  {role}: {count}")
    return "\n".join(lines)


def format_csv(listing: list[dict]) -> str:
    """Format a user listing as CSV."""
    if not listing:
        return ""
    headers = list(listing[0].keys())
    lines = [",".join(headers)]
    for row in listing:
        lines.append(",".join(str(row.get(h, "")) for h in headers))
    return "\n".join(lines)


def format_table(listing: list[dict], max_width: int = 80) -> str:
    """Format a user listing as a fixed-width text table."""
    if not listing:
        return "(empty)"
    headers = list(listing[0].keys())
    col_widths = {h: len(h) for h in headers}
    for row in listing:
        for h in headers:
            col_widths[h] = max(col_widths[h], len(str(row.get(h, ""))))

    header_line = " | ".join(h.ljust(col_widths[h]) for h in headers)
    separator = "-+-".join("-" * col_widths[h] for h in headers)
    data_lines = []
    for row in listing:
        data_lines.append(
            " | ".join(str(row.get(h, "")).ljust(col_widths[h]) for h in headers)
        )
    return "\n".join([header_line, separator] + data_lines)
