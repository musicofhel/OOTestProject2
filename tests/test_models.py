"""Tests for user data models."""
from oo_test_project2.models import User, UserSummary, list_users, summarize_users


class TestUser:
    def test_defaults(self):
        u = User(id=1, username="alice", email="alice@test.com")
        assert u.is_active is True
        assert u.role == "member"

    def test_custom_role(self):
        u = User(id=2, username="bob", email="bob@test.com", role="admin")
        assert u.role == "admin"


class TestListUsers:
    def test_default_limit(self):
        users = [User(id=i, username=f"u{i}", email=f"u{i}@t.com") for i in range(5)]
        result = list_users(users)
        assert len(result) == 5

    def test_with_limit(self):
        users = [User(id=i, username=f"u{i}", email=f"u{i}@t.com") for i in range(10)]
        result = list_users(users, limit=3)
        assert len(result) == 3
        assert result[0].id == 0
        assert result[2].id == 2

    def test_limit_exceeds_list(self):
        users = [User(id=1, username="a", email="a@t.com")]
        result = list_users(users, limit=100)
        assert len(result) == 1

    def test_empty(self):
        assert list_users([]) == []

    def test_limit_zero(self):
        users = [User(id=1, username="a", email="a@t.com")]
        assert list_users(users, limit=0) == []


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
