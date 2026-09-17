# Repository Instructions

These rules apply to every change in this repository. Project instructions define
the Dragon workflow, sprint files define sprint-specific behavior, and agent files
define role ownership. Do not copy those rules into another file.

## Engineering standards

- Use Python 3.14 or later.
- Use the Python standard library only; do not add dependencies unless requested.
- Follow PEP 8 and use four spaces for indentation.
- Use complete type annotations where they improve clarity.
- Prefer `pathlib` for filesystem paths.
- Use meaningful names and keep functions and classes focused.
- Add docstrings to new public functions and classes.
- Comment only non-obvious logic.
- Keep source code, identifiers, docstrings, and comments in English.
- Preserve public APIs unless the task explicitly changes them.

## Scope and quality

- Meet the stated acceptance criteria and do not add unrequested features.
- Treat the brief as the source of scope; do not invent product requirements.
- Do not commit generated artifacts such as bytecode, virtual environments,
  test caches, or local IDE state.
- Every behavior change must have deterministic, descriptive tests, including
  relevant edge cases. Follow the assigned agent's ownership rules for test
  files.
- Use the repository's existing test framework and run the smallest relevant
  validation command.
