"""Core domain objects for the dragon project."""

from dataclasses import dataclass


class DragonError(Exception):
    """Raised when Dragon creation fails validation."""
    pass


@dataclass(slots=True)
class Dragon:
    """Represent a dragon created in the system."""

    name: str

    def __post_init__(self) -> None:
        """Validate dragon attributes after initialization."""
        if not self.name or not self.name.strip():
            raise DragonError("Dragon name cannot be empty")
