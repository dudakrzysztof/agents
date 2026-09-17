"""Tests for the dragon project."""

from unittest import TestCase, main

from dragon import Dragon, DragonError


class DragonCreateTestCase(TestCase):
    """Cover dragon creation scenarios."""

    def test_create_dragon_with_name(self) -> None:
        """A created dragon should exist with the provided name."""
        dragon = Dragon(name="Wawelski")

        self.assertIsNotNone(dragon)
        self.assertEqual("Wawelski", dragon.name)

    def test_create_dragon_without_name_raises_error(self) -> None:
        """Creating a dragon without name should raise an error."""
        with self.assertRaises(DragonError) as context:
            Dragon(name="")

        self.assertEqual("Dragon name cannot be empty", str(context.exception))

    def test_create_dragon_with_empty_whitespace_raises_error(self) -> None:
        """Creating a dragon with only whitespace should raise an error."""
        with self.assertRaises(DragonError) as context:
            Dragon(name="   ")

        self.assertEqual("Dragon name cannot be empty", str(context.exception))


class DragonHealthTestCase(TestCase):
    """Cover dragon health scenarios."""

    def test_dragon_has_random_health_on_creation(self) -> None:
        """A created dragon should have random health between 50 and 100."""
        dragon = Dragon(name="Wawelski")

        self.assertIsNotNone(dragon.health)
        self.assertGreaterEqual(dragon.health, 50)
        self.assertLessEqual(dragon.health, 100)

    def test_dragon_health_varies_between_creations(self) -> None:
        """Multiple dragons should have different health values."""
        dragons = [Dragon(name=f"Dragon{i}") for i in range(10)]
        health_values = [dragon.health for dragon in dragons]

        self.assertGreater(len(set(health_values)), 1)


if __name__ == "__main__":
    main()
