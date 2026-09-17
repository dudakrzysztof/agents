"""Core domain objects for the dragon project."""

from dataclasses import dataclass
from random import randint


class DragonError(Exception):
    """Raised when Dragon creation fails validation."""
    pass


@dataclass(slots=True)
class Dragon:
    """Represent a dragon created in the system."""

    name: str
    health: int = 0
    position_x: int = 50
    position_y: int = 100

    def __post_init__(self) -> None:
        """Validate dragon attributes after initialization."""
        if not self.name or not self.name.strip():
            raise DragonError("Dragon name cannot be empty")
        self.health = randint(50, 100)

    def get_position(self) -> str:
        """Return the dragon's current position as a coordinate string."""
        return f"({self.position_x}, {self.position_y})"

    def set_position(self, position_x: int, position_y: int) -> None:
        """Set the dragon's current position."""
        self.position_x = position_x
        self.position_y = position_y

    def move_right(self, value: int) -> None:
        """Move the dragon right by the requested value."""
        self.position_x += value

    def move_left(self, value: int) -> None:
        """Move the dragon left by the requested value."""
        self.position_x -= value

    def move_down(self, value: int) -> None:
        """Move the dragon down by the requested value."""
        self.position_y += value

    def move_up(self, value: int) -> None:
        """Move the dragon up by the requested value."""
        self.position_y -= value

    def make_damage(self) -> int:
        """Return a random amount of damage between 5 and 20."""
        return randint(5, 20)
