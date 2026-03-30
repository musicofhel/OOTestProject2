"""Report generation from user data."""
from oo_test_project2.models import User, UserSummary, summarize_users


def generate_summary_report(users: list[User]) -> dict:
    """Generate a summary report from user records.

    Returns a dict with keys: total, active, inactive, active_rate, roles.
    """
    summary = summarize_users(users)
    return {
        "total": summary.total_users,
        "active": summary.active_users,
        "inactive": summary.inactive_users,
        "active_rate": round(summary.active_rate, 2),
        "roles": summary.roles,
    }


def generate_user_listing(
    users: list[User],
    *,
    active_only: bool = False,
    role_filter: str | None = None,
) -> list[dict]:
    """Generate a filtered user listing.

    Args:
        users: Source user records.
        active_only: If True, exclude inactive users.
        role_filter: If set, include only users with this role.

    Returns:
        List of user dicts with id, username, email, role.
    """
    filtered = users
    if active_only:
        filtered = [u for u in filtered if u.is_active]
    if role_filter:
        filtered = [u for u in filtered if u.role == role_filter]
    return [
        {"id": u.id, "username": u.username, "email": u.email, "role": u.role}
        for u in filtered
    ]
