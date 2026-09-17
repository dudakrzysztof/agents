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

    def __post_init__(self) -> None:
        """Validate dragon attributes after initialization."""
        if not self.name or not self.name.strip():
            raise DragonError("Dragon name cannot be empty")
        self.health = randint(50, 100)
