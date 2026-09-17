"""Tests for the dragon project."""

from unittest import TestCase, main
from unittest.mock import call, patch

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


class DragonDamageTestCase(TestCase):
    """Cover dragon damage scenarios."""

    def test_dragon_makes_damage_between_five_and_twenty(self) -> None:
        """A dragon should make damage within the sprint-defined range."""
        dragon = Dragon(name="Wawelski")

        damage = dragon.make_damage()

        self.assertIsInstance(damage, int)
        self.assertGreaterEqual(damage, 5)
        self.assertLessEqual(damage, 20)

    def test_dragon_makes_damage_at_inclusive_bounds(self) -> None:
        """Damage generation should include both range boundaries."""
        dragon = Dragon(name="Wawelski")

        with patch("dragon.dragon.randint", side_effect=[5, 20]) as randint_mock:
            self.assertEqual(5, dragon.make_damage())
            self.assertEqual(20, dragon.make_damage())

        self.assertEqual(
            [call(5, 20), call(5, 20)],
            randint_mock.call_args_list,
        )


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

    def test_dragon_can_be_set_at_any_position(self) -> None:
        """A dragon should move to the position provided by the caller."""
        dragon = Dragon(name="Wawelski")

        dragon.set_position(position_x=1, position_y=2)

        self.assertEqual(1, dragon.position_x)
        self.assertEqual(2, dragon.position_y)

    def test_dragon_moves_right(self) -> None:
        """Moving right should increase only the x coordinate."""
        dragon = Dragon(name="Wawelski", position_x=10, position_y=20)

        dragon.move_right(1)

        self.assertEqual(11, dragon.position_x)
        self.assertEqual(20, dragon.position_y)

    def test_dragon_moves_left(self) -> None:
        """Moving left should decrease only the x coordinate."""
        dragon = Dragon(name="Wawelski", position_x=10, position_y=20)

        dragon.move_left(1)

        self.assertEqual(9, dragon.position_x)
        self.assertEqual(20, dragon.position_y)

    def test_dragon_moves_down(self) -> None:
        """Moving down should increase only the y coordinate."""
        dragon = Dragon(name="Wawelski", position_x=10, position_y=20)

        dragon.move_down(1)

        self.assertEqual(10, dragon.position_x)
        self.assertEqual(21, dragon.position_y)

    def test_dragon_moves_up(self) -> None:
        """Moving up should decrease only the y coordinate."""
        dragon = Dragon(name="Wawelski", position_x=10, position_y=20)

        dragon.move_up(1)

        self.assertEqual(10, dragon.position_x)
        self.assertEqual(19, dragon.position_y)

    def test_dragon_moves_horizontally(self) -> None:
        """Opposing horizontal movements should accumulate on the x axis."""
        dragon = Dragon(name="Wawelski", position_x=10, position_y=20)

        dragon.move_right(1)
        dragon.move_left(2)

        self.assertEqual(9, dragon.position_x)
        self.assertEqual(20, dragon.position_y)

    def test_dragon_moves_vertically(self) -> None:
        """Opposing vertical movements should accumulate on the y axis."""
        dragon = Dragon(name="Wawelski", position_x=10, position_y=20)

        dragon.move_down(1)
        dragon.move_up(2)

        self.assertEqual(10, dragon.position_x)
        self.assertEqual(19, dragon.position_y)

    def test_dragon_moves_omnidirectionally(self) -> None:
        """Movement in all directions should update both coordinates."""
        dragon = Dragon(name="Wawelski", position_x=10, position_y=20)

        dragon.move_right(1)
        dragon.move_left(2)
        dragon.move_down(3)
        dragon.move_up(4)

        self.assertEqual(9, dragon.position_x)
        self.assertEqual(19, dragon.position_y)

    def test_dragon_applies_the_movement_use_case(self) -> None:
        """The documented movement sequence should produce the final position."""
        dragon = Dragon(name="Wawelski", position_x=10, position_y=20)

        dragon.move_left(10)
        dragon.move_down(20)
        dragon.move_left(10)
        dragon.move_right(15)
        dragon.move_right(15)
        dragon.move_up(5)
        dragon.move_down(5)

        self.assertEqual(20, dragon.position_x)
        self.assertEqual(40, dragon.position_y)

    def test_dragon_moves_by_relative_x_and_y_offsets(self) -> None:
        """A single move should apply arbitrary horizontal and vertical offsets."""
        dragon = Dragon(name="Wawelski", position_x=10, position_y=20)

        dragon.move(x=-25, y=35)

        self.assertEqual(-15, dragon.position_x)
        self.assertEqual(55, dragon.position_y)


if __name__ == "__main__":
    main()
