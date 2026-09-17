# Dragon Project Instructions

## Overview
The Dragon project is an MVP business requirements exercise. Treat it as a programming task, not game development.

## Implementation Flow

1. **Check current status**
   - Review `/dragon/README.md` for implemented features
   - Run tests: `python -m unittest dragon_tests -v`
   - Ensure all tests pass before starting

2. **Review sprint requirements**
   - When the user says `robimy Sprint N`, read `.github\instructions\sprint\sprint-N.md`.
   - If the file does not exist, ask the user to create it; do not fetch requirements from the web.
   - Treat the selected local sprint file as authoritative.

3. **Implement focused solution**
   - Implement only what's requested
   - Extend previous sprint code
   - Keep code minimal and focused
   - Add docstrings to all new functions and classes
   - Add or update tests and update `/dragon/README.md`
   - Run the test suite after implementation
   - Create a commit named `Sprint NN: ...`
   - Push only when the user explicitly requests it

4. **Write tests**
   - Add tests for new behavior
   - All tests must pass
   - Include edge cases

5. **Update and commit**
   - Update `/dragon/README.md` with new features
   - Commit with descriptive message
   - Include "Sprint XX:" prefix in message

## Principles
- Respect the brief: you are the programmer, not the PO
- Keep solutions focused on stated requirements
- Prefer TDD, KISS, DRY, SOLID
- Avoid over-engineering

## Repository Structure
```
dragon/
├── __init__.py          - public package API
├── dragon.py            - core domain objects
├── dragon_tests.py      - unit tests
└── README.md            - current capabilities
```
