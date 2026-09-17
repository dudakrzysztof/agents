# Dragon

This package contains the Dragon MVP used for the `python3.info` training tasks.

## Project structure

- `dragon/__init__.py` exposes the public package API
- `dragon/dragon.py` contains the core domain object
- `dragon/dragon_tests.py` contains the unit tests
- `dragon/README.md` documents the current sprint scope

## Current implementation

The project currently supports:
- Creating a `Dragon` instance with a `name` field
- Validating that the dragon name is not empty (raises `DragonError` if empty)
- Assigning random health points (50-100) to each dragon on creation
- Starting a dragon at the default position `(x=0, y=0)`
- Creating a dragon with a custom initial `x` and `y` position

## Notes

- The implementation uses only the Python standard library.
- The solution is intentionally small and focused on the current acceptance criteria.
- Dragon creation raises `DragonError` when the name is empty or contains only whitespace.
- Dragon health is randomly assigned between 50 and 100 (inclusive) using `random.randint()`.
- Dragon coordinates are set to `x=0` and `y=0` by default and can be customized at creation.
