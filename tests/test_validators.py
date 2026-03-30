"""Tests for schema validation."""
from oo_test_project2.validators import validate_user_record, validate_batch


class TestValidateUserRecord:
    def test_valid_minimal(self):
        errs = validate_user_record({"id": 1, "username": "a", "email": "a@t.com"})
        assert errs == []

    def test_valid_full(self):
        errs = validate_user_record({
            "id": 1, "username": "a", "email": "a@t.com",
            "is_active": True, "role": "admin",
        })
        assert errs == []

    def test_missing_required(self):
        errs = validate_user_record({"username": "a"})
        assert any("id" in e for e in errs)
        assert any("email" in e for e in errs)

    def test_unknown_field(self):
        errs = validate_user_record({"id": 1, "username": "a", "email": "a@t.com", "bogus": 42})
        assert any("Unknown field" in e for e in errs)

    def test_wrong_type(self):
        errs = validate_user_record({"id": "not-int", "username": "a", "email": "a@t.com"})
        assert any("must be int" in e for e in errs)

    def test_invalid_role(self):
        errs = validate_user_record({"id": 1, "username": "a", "email": "a@t.com", "role": "superadmin"})
        assert any("Invalid role" in e for e in errs)

    def test_invalid_email(self):
        errs = validate_user_record({"id": 1, "username": "a", "email": "not-an-email"})
        assert any("Invalid email" in e for e in errs)


class TestValidateBatch:
    def test_all_valid(self):
        records = [
            {"id": 1, "username": "a", "email": "a@t.com"},
            {"id": 2, "username": "b", "email": "b@t.com"},
        ]
        result = validate_batch(records)
        assert result["valid_count"] == 2
        assert result["invalid_count"] == 0

    def test_mixed(self):
        records = [
            {"id": 1, "username": "a", "email": "a@t.com"},
            {"id": "bad", "username": "b"},  # missing email, bad id type
        ]
        result = validate_batch(records)
        assert result["valid_count"] == 1
        assert result["invalid_count"] == 1
        assert len(result["errors"]) == 1
        assert result["errors"][0][0] == 1  # index of bad record
