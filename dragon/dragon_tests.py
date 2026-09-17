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
        dragons = [
            Dragon(name=f"Dragon{dragon_index}")
            for dragon_index in range(10)
        ]
        health_values = [dragon.health for dragon in dragons]

        self.assertGreater(len(set(health_values)), 1)


class DragonPositionTestCase(TestCase):
    """Cover dragon position scenarios."""

    def test_dragon_has_default_position_on_creation(self) -> None:
        """A created dragon should start at the sprint-defined position."""
        dragon = Dragon(name="Wawelski")

        self.assertEqual(50, dragon.position_x)
        self.assertEqual(100, dragon.position_y)

    def test_dragon_can_be_created_with_initial_position(self) -> None:
        """A created dragon should retain its provided position."""
        dragon = Dragon(name="Wawelski", position_x=50, position_y=100)

        self.assertEqual(50, dragon.position_x)
        self.assertEqual(100, dragon.position_y)

    def test_dragon_returns_current_position(self) -> None:
        """A dragon should return its current position in coordinate format."""
        dragon = Dragon(name="Wawelski")
        dragon.position_x = 1
        dragon.position_y = 2

        self.assertEqual("(1, 2)", dragon.get_position())


if __name__ == "__main__":
    main()
