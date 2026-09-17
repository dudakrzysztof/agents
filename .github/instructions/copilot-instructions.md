# Copilot Instructions

## General Guidelines

### Code Principles
- Provide clear, well-documented code
- Follow Python best practices and PEP 8
- Use Python 3.14+
- Include type hints where applicable
- Write meaningful variable and function names
- Solutions in English
- Standard library only, no external dependencies

### Implementation Constraints
- Meet all acceptance criteria
- Don't add unrequested features
- Respect the brief: you are the programmer, not the PO

### Code Style
- 4 spaces indentation (Python)
- Docstrings for functions and classes
- Comments for complex logic
- Keep functions focused and modular

### Testing
- Write tests alongside implementations
- Descriptive test case names
- Include edge case testing

## Project-Specific Guidelines

See [DRAGON.md](./DRAGON.md) for Dragon project details.

### Current Dragon Implementation (Sprint 03)

**Features:**
- `Dragon` dataclass with `name` (validated, non-empty) and `health` (random 50-100)
- `DragonError` exception for validation failures
- Comprehensive test suite (5 passing tests)

**Structure:**
```
dragon/
├── __init__.py          - exports Dragon, DragonError
├── dragon.py            - core implementation (~24 LOC)
├── dragon_tests.py      - unit tests (5 test cases)
└── README.md            - sprint documentation
```

**Before starting new work:** Review sprint requirements at https://python3.info/dragon/polish/sprint-XX.html and ensure all current tests still pass.
