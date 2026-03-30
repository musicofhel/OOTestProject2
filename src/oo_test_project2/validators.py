"""Schema validation for user data.

Validates that incoming user records match the expected schema from
OOTestProject1. When the upstream schema changes, validation rules
here must be updated to match.
"""


REQUIRED_FIELDS = {"id", "username", "email"}
OPTIONAL_FIELDS = {"created_at", "is_active", "role"}
VALID_ROLES = {"member", "admin", "viewer"}


def validate_user_record(record: dict) -> list[str]:
    """Validate a raw user record dict.

    Returns a list of error strings. Empty list means valid.
    """
    errors = []

    # Check required fields
    for field in REQUIRED_FIELDS:
        if field not in record:
            errors.append(f"Missing required field: {field}")

    # Check for unknown fields
    known = REQUIRED_FIELDS | OPTIONAL_FIELDS
    for key in record:
        if key not in known:
            errors.append(f"Unknown field: {key}")

    # Type checks
    if "id" in record and not isinstance(record["id"], int):
        errors.append(f"Field 'id' must be int, got {type(record['id']).__name__}")
    if "username" in record and not isinstance(record["username"], str):
        errors.append("Field 'username' must be str")
    if "email" in record and not isinstance(record["email"], str):
        errors.append("Field 'email' must be str")
    if "is_active" in record and not isinstance(record["is_active"], bool):
        errors.append("Field 'is_active' must be bool")

    # Value checks
    if "role" in record and record["role"] not in VALID_ROLES:
        errors.append(f"Invalid role: {record['role']}. Must be one of {VALID_ROLES}")
    if "email" in record and isinstance(record["email"], str) and "@" not in record["email"]:
        errors.append(f"Invalid email: {record['email']}")

    return errors


def validate_batch(records: list[dict]) -> dict:
    """Validate a batch of user records.

    Returns:
        Dict with keys: valid_count, invalid_count, errors (list of (index, errors) tuples).
    """
    valid = 0
    invalid = 0
    all_errors = []
    for i, record in enumerate(records):
        errs = validate_user_record(record)
        if errs:
            invalid += 1
            all_errors.append((i, errs))
        else:
            valid += 1
    return {"valid_count": valid, "invalid_count": invalid, "errors": all_errors}
