"""Tests for output formatters."""
from oo_test_project2.formatters import format_text, format_csv, format_table


class TestFormatText:
    def test_basic(self):
        report = {"total": 10, "active": 8, "inactive": 2, "active_rate": 0.8, "roles": {"admin": 2, "member": 8}}
        text = format_text(report)
        assert "Total users: 10" in text
        assert "Active: 8" in text
        assert "admin: 2" in text


class TestFormatCsv:
    def test_basic(self):
        listing = [{"id": 1, "username": "a", "email": "a@t.com", "role": "admin"}]
        csv = format_csv(listing)
        assert "id,username,email,role" in csv
        assert "1,a,a@t.com,admin" in csv

    def test_empty(self):
        assert format_csv([]) == ""


class TestFormatTable:
    def test_basic(self):
        listing = [{"id": 1, "name": "alice"}, {"id": 2, "name": "bob"}]
        table = format_table(listing)
        assert "alice" in table
        assert "bob" in table
        assert "---" in table  # separator

    def test_empty(self):
        assert format_table([]) == "(empty)"
