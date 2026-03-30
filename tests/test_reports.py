"""Tests for report generation."""
from oo_test_project2.models import User
from oo_test_project2.reports import (
    generate_limited_summary,
    generate_summary_report,
    generate_user_listing,
)


class TestSummaryReport:
    def test_basic(self):
        users = [
            User(id=1, username="a", email="a@t.com"),
            User(id=2, username="b", email="b@t.com", is_active=False),
        ]
        report = generate_summary_report(users)
        assert report["total"] == 2
        assert report["active"] == 1
        assert report["active_rate"] == 0.5

    def test_empty(self):
        report = generate_summary_report([])
        assert report["total"] == 0
        assert report["active_rate"] == 0.0


class TestLimitedSummary:
    def test_limits_users(self):
        users = [
            User(id=1, username="a", email="a@t.com"),
            User(id=2, username="b", email="b@t.com"),
            User(id=3, username="c", email="c@t.com"),
        ]
        report = generate_limited_summary(users, limit=2)
        assert report["total"] == 2

    def test_default_limit(self):
        users = [User(id=i, username=f"u{i}", email=f"u{i}@t.com") for i in range(5)]
        report = generate_limited_summary(users)
        assert report["total"] == 5


class TestUserListing:
    def test_all_users(self):
        users = [
            User(id=1, username="a", email="a@t.com"),
            User(id=2, username="b", email="b@t.com"),
        ]
        listing = generate_user_listing(users)
        assert len(listing) == 2
        assert listing[0]["username"] == "a"

    def test_active_only(self):
        users = [
            User(id=1, username="a", email="a@t.com", is_active=True),
            User(id=2, username="b", email="b@t.com", is_active=False),
        ]
        listing = generate_user_listing(users, active_only=True)
        assert len(listing) == 1
        assert listing[0]["username"] == "a"

    def test_role_filter(self):
        users = [
            User(id=1, username="a", email="a@t.com", role="admin"),
            User(id=2, username="b", email="b@t.com", role="member"),
        ]
        listing = generate_user_listing(users, role_filter="admin")
        assert len(listing) == 1
        assert listing[0]["role"] == "admin"
