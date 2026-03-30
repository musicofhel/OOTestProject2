"""Tests for user data models."""
from oo_test_project2.models import User, UserSummary, summarize_users


class TestUser:
    def test_defaults(self):
        u = User(id=1, username="alice", email="alice@test.com")
        assert u.is_active is True
        assert u.role == "member"

    def test_custom_role(self):
        u = User(id=2, username="bob", email="bob@test.com", role="admin")
        assert u.role == "admin"


class TestSummarizeUsers:
    def test_empty(self):
        s = summarize_users([])
        assert s.total_users == 0
        assert s.active_rate == 0.0

    def test_all_active(self):
        users = [
            User(id=1, username="a", email="a@t.com"),
            User(id=2, username="b", email="b@t.com"),
        ]
        s = summarize_users(users)
        assert s.total_users == 2
        assert s.active_users == 2
        assert s.active_rate == 1.0

    def test_mixed_active(self):
        users = [
            User(id=1, username="a", email="a@t.com", is_active=True),
            User(id=2, username="b", email="b@t.com", is_active=False),
        ]
        s = summarize_users(users)
        assert s.active_users == 1
        assert s.inactive_users == 1
        assert s.active_rate == 0.5

    def test_role_counts(self):
        users = [
            User(id=1, username="a", email="a@t.com", role="admin"),
            User(id=2, username="b", email="b@t.com", role="member"),
            User(id=3, username="c", email="c@t.com", role="admin"),
        ]
        s = summarize_users(users)
        assert s.roles == {"admin": 2, "member": 1}
