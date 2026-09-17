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


if __name__ == "__main__":
    main()
