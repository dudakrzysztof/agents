"""Core domain objects for the dragon project."""

from dataclasses import dataclass, field
from random import randint


class DragonError(Exception):
    """Raised when a dragon receives invalid input."""

    pass


@dataclass(slots=True)
class Dragon:
    """Represent a dragon created in the system."""

    name: str
    health: int = field(init=False, default_factory=lambda: randint(50, 100))
    position_x: int = 50
    position_y: int = 100

    def __post_init__(self) -> None:
        """Validate dragon attributes after initialization."""
        if not isinstance(self.name, str):
            raise DragonError("Dragon name must be a string")
        if not self.name.strip():
            raise DragonError("Dragon name cannot be empty")
        self._validate_integer(self.position_x, "position_x")
        self._validate_integer(self.position_y, "position_y")

    @staticmethod
    def _validate_integer(value: object, parameter_name: str) -> None:
        """Require an integer value while excluding booleans."""
        if isinstance(value, bool) or not isinstance(value, int):
            raise DragonError(f"{parameter_name} must be an integer")

    @property
    def position(self) -> tuple[int, int]:
        """Return the current position as an (x, y) tuple."""
        return self.position_x, self.position_y

    def get_position(self) -> str:
        """Return the dragon's current position as a coordinate string."""
        return f"({self.position_x}, {self.position_y})"

    def set_position(self, position_x: int, position_y: int) -> None:
        """Set the dragon's current position."""
        self._validate_integer(position_x, "position_x")
        self._validate_integer(position_y, "position_y")
        self.position_x = position_x
        self.position_y = position_y

    def move_right(self, value: int) -> None:
        """Move the dragon right by the requested value."""
        self._validate_integer(value, "value")
        self.move(x=value)

    def move_left(self, value: int) -> None:
        """Move the dragon left by the requested value."""
        self._validate_integer(value, "value")
        self.move(x=-value)

    def move_down(self, value: int) -> None:
        """Move the dragon down by the requested value."""
        self._validate_integer(value, "value")
        self.move(y=value)

    def move_up(self, value: int) -> None:
        """Move the dragon up by the requested value."""
        self._validate_integer(value, "value")
        self.move(y=-value)

    def move(self, x: int = 0, y: int = 0) -> None:
        """Move by relative offsets: positive x is right and positive y is down."""
        self._validate_integer(x, "x")
        self._validate_integer(y, "y")
        self.position_x += x
        self.position_y += y

    def make_damage(self) -> int:
        """Return a random amount of damage between 5 and 20."""
        return randint(5, 20)
