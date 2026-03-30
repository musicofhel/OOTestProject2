"""User data models — mirrors OOTestProject1 db schema.

This module defines the data structures that OOTestProject2 uses to
consume user records. The schema must stay in sync with
OOTestProject1's src/oo_test_project/db/users.py.

When OOTestProject1 changes its user schema (adds fields, renames
columns, changes types), this file and its dependents need updating.
"""
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class User:
    """User record matching the upstream schema."""
    id: int
    username: str
    email: str
    created_at: datetime | None = None
    is_active: bool = True
    role: str = "member"


@dataclass
class UserSummary:
    """Aggregated user statistics for reports."""
    total_users: int = 0
    active_users: int = 0
    inactive_users: int = 0
    roles: dict[str, int] = field(default_factory=dict)

    @property
    def active_rate(self) -> float:
        if self.total_users == 0:
            return 0.0
        return self.active_users / self.total_users


def summarize_users(users: list[User]) -> UserSummary:
    """Build a UserSummary from a list of User records."""
    summary = UserSummary(total_users=len(users))
    roles: dict[str, int] = {}
    for user in users:
        if user.is_active:
            summary.active_users += 1
        else:
            summary.inactive_users += 1
        roles[user.role] = roles.get(user.role, 0) + 1
    summary.roles = roles
    return summary
