# OOTestProject2

Downstream test target for the [dev-loop](https://github.com/musicofhel/dev-loop) harness.

Depends on [OOTestProject1](https://github.com/musicofhel/OOTestProject1)'s user data model. When OOTestProject1's `db/` schema changes, this repo's validators and reports need to adapt.

## Structure

- `models.py` — User data models (mirrors upstream schema)
- `reports.py` — Report generation from user data
- `formatters.py` — Output formatting (text, CSV, table)
- `validators.py` — Schema validation for incoming data

## Run tests

```bash
uv run pytest -v
```

## Cascade relationship

In the dev-loop harness, OOTestProject1 is the cascade **source** and OOTestProject2 is the **target**:

```
OOTestProject1 (src/oo_test_project/db/**) → OOTestProject2
```

When files matching `src/oo_test_project/db/**` change in OOTestProject1, dev-loop creates a cascade issue in OOTestProject2 prompting the agent to review and adapt.
