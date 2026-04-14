
# Dev-Loop Agent Instructions

## Issue: [cascade] Adapt to upstream changes from bd-t7r: Add email field to user model in db/users.py

### Description

Upstream issue bd-t7r (Add email field to user model in db/users.py) changed files matching watch patterns:
  src/oo_test_project/db/**

Dependency type: data-model.

Changed files in source repo:
  - src/oo_test_project/db/users.py

Action required:
- Review OOTestProject2's code that depends on the upstream schema/API
- Update validators, models, or data structures as needed
- Run the test suite and fix any failures caused by upstream changes

Acceptance criteria:
- All existing tests pass after adapting to upstream changes
- No schema mismatches between upstream and downstream models

## Persona: feature

Implement the feature as described in the issue.
Write tests for new code. Follow existing patterns.

## Setup

- Before running tests, install the project in the worktree:
  `uv sync --dev` (or `pip install -e '.[dev]'` if uv is not available)
- If pyproject.toml or setup.py exists, always install before running pytest.

## Rules

- Work only on the issue described above.
- Do not modify files outside the scope of this issue.
- Commit your changes with a clear message referencing the issue ID.
- If you are blocked or unsure, stop and report rather than guessing.

## Context Window Management

- If you notice your context window is getting large (above ~75%), commit your current changes immediately.
- Write a brief handoff note to `/tmp/dev-loop/handoffs/bd-2i7.md` describing: what is done, what files were changed, what remains to be done, and any important context for a fresh session.
- Then exit cleanly. A fresh session will pick up where you left off.

## NEVER read these files
- .env, .env.*, *.key, *.pem, *.p12, *.pfx, credentials.*, *secret*
- .aws/*, .ssh/*, *.keystore, *.jks, .netrc, .npmrc, .pypirc
If you need data from these files, ask the human.

## In-Process Feedback

Run checks frequently during your work — do not wait until the end.

- After editing Python files, run `uv run pytest --tb=short -q` on affected test files.
- If the project uses type checking (mypy/pyright), run it after edits.
- Fix any errors before moving to the next file.


## Code Verification

- Always read a function's implementation before calling it. Never assume what a function does from its name alone.
- Before importing a module, verify it exists in the project.
- Before using an API endpoint, verify it exists in the route definitions.
- If you are unsure whether a function/class/module exists, search for it first.


## Lock File Rules

- After modifying `pyproject.toml` dependencies, run `uv lock` to keep the lock file in sync.


## Repository Structure

**16 tracked files**
Languages: Python (10), YAML (2), Markdown (1), TOML (1)

```
src                               5 files
tests                             5 files
.                                 3 files
.beads                            2 files
.github                           1 files
```

## Focus Areas

The following paths appear relevant to this issue — start your investigation here:

- `src`
