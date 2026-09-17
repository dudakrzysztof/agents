# Dragon

This package contains the Dragon MVP used for the `python3.info` training tasks.

## Project structure

- `dragon/__init__.py` exposes the public package API
- `dragon/dragon.py` contains the core domain object
- `dragon/dragon_tests.py` contains the unit tests
- `dragon/dragon_behavioral_tests.py` contains behavioral acceptance tests
- `dragon/README.md` documents the current sprint scope

## Current implementation

The project currently supports:
- Creating a `Dragon` instance with a `name` field
- Validating that the dragon name is not empty (raises `DragonError` if empty)
- Assigning random health points (50-100) to each dragon on creation
- Starting a dragon at the default position `(50, 100)`
- Creating a dragon with custom `position_x` and `position_y` values
- Returning the current position in the `(x, y)` format
- Setting the current position with `Dragon.set_position()`
- Moving right, left, down, or up by a requested value
- Moving by relative x and y offsets with `Dragon.move()`

## Notes

- The implementation uses only the Python standard library.
- The solution is intentionally small and focused on the current acceptance criteria.
- Dragon creation raises `DragonError` when the name is empty or contains only whitespace.
- Dragon health is randomly assigned between 50 and 100 (inclusive) using `random.randint()`.
- Dragon coordinates are stored in `position_x` and `position_y`, defaulting to `50` and `100`, and can be customized at creation.
- The current position is available through `Dragon.get_position()`.
- The current position can be changed through `Dragon.set_position(position_x, position_y)`.
- Relative movement uses `Dragon.move_right()`, `Dragon.move_left()`,
  `Dragon.move_down()`, and `Dragon.move_up()`. Right and down increase the
  corresponding coordinate; left and up decrease it.
- Combined movement uses `Dragon.move(x, y)`, where positive x moves right,
  negative x moves left, positive y moves down, and negative y moves up.
- Returning random damage between 5 and 20 through `Dragon.make_damage()`.
