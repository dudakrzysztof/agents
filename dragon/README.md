# Dragon

Dragon is a small, dependency-free Python domain model for representing a
dragon with health, a two-dimensional position, movement, and random damage.
It is designed as an educational MVP and as a simple foundation for
coordinate-based game or simulation prototypes.

## Features

- Create a named dragon with automatic validation.
- Assign random health between 50 and 100 inclusive at creation time.
- Start at `(50, 100)` or provide a custom initial position.
- Read or set the absolute position.
- Move by a signed `(x, y)` offset in one operation.
- Move in a single direction when a directional method is more expressive.
- Generate random damage between 5 and 20 inclusive.

## Requirements

- Python 3.14 or later
- Python standard library only

## Quick start

```python
from dragon import Dragon

dragon = Dragon(name="Wawelski")

print(dragon.name)          # Wawelski
print(dragon.health)        # A value from 50 to 100
print(dragon.position)      # (50, 100)
print(dragon.get_position())  # (50, 100)

dragon.set_position(position_x=10, position_y=20)
dragon.move(x=-25, y=35)

print(dragon.get_position())  # (-15, 55)
```

`Dragon.move()` applies relative offsets. Positive `x` moves right, negative
`x` moves left, positive `y` moves down, and negative `y` moves up.

## Usage examples

### Combining horizontal and vertical movement

Use one `move()` call instead of invoking several single-direction methods:

```python
dragon.set_position(position_x=10, position_y=20)
dragon.move(x=15, y=-5)

assert dragon.get_position() == "(25, 15)"
```

### Moving in one direction

Directional methods remain available when they make the intent clearer:

```python
dragon.move_right(10)
dragon.move_left(4)
dragon.move_down(20)
dragon.move_up(5)
```

### Generating damage

```python
damage = dragon.make_damage()

assert 5 <= damage <= 20
```

The damage value is returned to the caller; the current implementation does
not apply damage to another object or reduce the dragon's own health.

### Handling invalid names

An empty or whitespace-only name raises `DragonError`:

```python
from dragon import Dragon, DragonError

try:
    Dragon(name=" ")
except DragonError as error:
    print(error)
```

Names must be strings. Initial and absolute position coordinates and all
movement offsets must be integers (not booleans); invalid values raise
`DragonError`. Coordinates and offsets may be negative.

## Public API

| API | Description |
| --- | --- |
| `Dragon(name, position_x=50, position_y=100)` | Create a dragon with validated name and random health. |
| `position` | Read the current position as an `(x, y)` tuple. |
| `get_position()` | Return the current position as a string in `(x, y)` format. |
| `set_position(position_x, position_y)` | Set an absolute position. |
| `move(x=0, y=0)` | Apply relative horizontal and vertical offsets. |
| `move_right(value)` / `move_left(value)` | Change the x coordinate. |
| `move_down(value)` / `move_up(value)` | Change the y coordinate. |
| `make_damage()` | Return a random integer from 5 to 20 inclusive. |

## Project structure

```text
dragon/
├── __init__.py                 Public package API
├── dragon.py                   Dragon and DragonError implementations
├── dragon_tests.py             Unit and regression tests
├── dragon_behavioral_tests.py  Behavioral acceptance tests
└── README.md                   Project documentation
```

## Running the tests

Run the complete test suite from the repository root:

```powershell
python -m unittest dragon.dragon_tests dragon.dragon_behavioral_tests -v
```
