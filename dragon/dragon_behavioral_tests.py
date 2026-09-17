"""Behavioral acceptance tests for the Dragon project."""

from unittest import TestCase, main
from unittest.mock import patch

from dragon import Dragon, DragonError


class DragonPositionBehaviorTestCase(TestCase):
    """Cover the Sprint 07 position scenarios."""

    @staticmethod
    def _given_dragon_at_position() -> Dragon:
        """Create the dragon used by the position scenarios."""
        dragon = Dragon(name="Wawelski")
        dragon.set_position(position_x=10, position_y=20)
        return dragon

    def _then_position_is(
        self, dragon: Dragon, position_x: int, position_y: int
    ) -> None:
        """Assert the position through the public position API."""
        self.assertEqual(
            f"({position_x}, {position_y})",
            dragon.get_position(),
        )

    def test_scenario_dragon_moves_right(self) -> None:
        """Given (10, 20), moving right by 1 results in (11, 20)."""
        dragon = self._given_dragon_at_position()

        dragon.move_right(1)

        self._then_position_is(dragon, position_x=11, position_y=20)

    def test_scenario_dragon_moves_left(self) -> None:
        """Given (10, 20), moving left by 1 results in (9, 20)."""
        dragon = self._given_dragon_at_position()

        dragon.move_left(1)

        self._then_position_is(dragon, position_x=9, position_y=20)

    def test_scenario_dragon_moves_down(self) -> None:
        """Given (10, 20), moving down by 1 results in (10, 21)."""
        dragon = self._given_dragon_at_position()

        dragon.move_down(1)

        self._then_position_is(dragon, position_x=10, position_y=21)

    def test_scenario_dragon_moves_up(self) -> None:
        """Given (10, 20), moving up by 1 results in (10, 19)."""
        dragon = self._given_dragon_at_position()

        dragon.move_up(1)

        self._then_position_is(dragon, position_x=10, position_y=19)

    def test_scenario_dragon_moves_horizontally(self) -> None:
        """Given (10, 20), right 1 and left 2 result in (9, 20)."""
        dragon = self._given_dragon_at_position()

        dragon.move_right(1)
        dragon.move_left(2)

        self._then_position_is(dragon, position_x=9, position_y=20)

    def test_scenario_dragon_moves_vertically(self) -> None:
        """Given (10, 20), down 1 and up 2 result in (10, 19)."""
        dragon = self._given_dragon_at_position()

        dragon.move_down(1)
        dragon.move_up(2)

        self._then_position_is(dragon, position_x=10, position_y=19)

    def test_scenario_dragon_moves_omnidirectionally(self) -> None:
        """Given (10, 20), all four movements result in (9, 19)."""
        dragon = self._given_dragon_at_position()

        dragon.move_right(1)
        dragon.move_left(2)
        dragon.move_down(3)
        dragon.move_up(4)

        self._then_position_is(dragon, position_x=9, position_y=19)

    def test_use_case_movement_sequence_with_move(self) -> None:
        """The Sprint 07 use case works with combined relative movement."""
        dragon = Dragon(name="Wawelski")
        self.assertEqual("(50, 100)", dragon.get_position())

        dragon.set_position(position_x=10, position_y=20)
        dragon.move(x=-10, y=20)
        dragon.move(x=5)
        dragon.move(x=15, y=-5)
        dragon.move(y=5)

        self._then_position_is(dragon, position_x=20, position_y=40)

    def test_scenario_dragon_moves_by_x_and_y_offsets(self) -> None:
        """A single call should move a dragon in two directions."""
        dragon = self._given_dragon_at_position()

        dragon.move(x=-25, y=35)

        self._then_position_is(dragon, position_x=-15, position_y=55)

    def test_scenario_position_is_available_as_a_read_only_tuple(self) -> None:
        """Position has a tuple view while the existing string API still works."""
        dragon = self._given_dragon_at_position()

        dragon.move(x=-25, y=35)

        self.assertEqual((-15, 55), dragon.position)
        self.assertEqual("(-15, 55)", dragon.get_position())
        with self.assertRaises(AttributeError):
            dragon.position = (0, 0)
        self.assertEqual((-15, 55), dragon.position)

    def test_scenario_signed_coordinates_and_offsets_are_accepted(self) -> None:
        """A dragon may start negative and move with signed integer offsets."""
        dragon = Dragon(name="Wawelski", position_x=-10, position_y=-20)

        dragon.set_position(position_x=-30, position_y=-40)
        dragon.move(x=-5, y=7)
        dragon.move_right(-2)
        dragon.move_up(-3)

        self.assertEqual((-37, -30), dragon.position)

    def test_scenario_invalid_absolute_position_does_not_partially_move(self) -> None:
        """Validation failure on the second coordinate leaves both unchanged."""
        dragon = self._given_dragon_at_position()

        with self.assertRaises(DragonError):
            dragon.set_position(position_x=99, position_y=False)

        self.assertEqual((10, 20), dragon.position)

    def test_scenario_invalid_movement_offsets_raise_dragon_error(self) -> None:
        """Combined and directional movement reject public non-integer inputs."""
        scenarios = (
            ("move", {"x": 1, "y": "down"}),
            ("move_right", {"value": True}),
            ("move_left", {"value": 1.5}),
            ("move_down", {"value": None}),
            ("move_up", {"value": False}),
        )

        for method_name, arguments in scenarios:
            with self.subTest(method_name=method_name):
                dragon = self._given_dragon_at_position()

                with self.assertRaises(DragonError):
                    getattr(dragon, method_name)(**arguments)

                self.assertEqual((10, 20), dragon.position)


class DragonCreationBehaviorTestCase(TestCase):
    """Cover creation and validation acceptance scenarios."""

    def test_scenario_health_uses_both_inclusive_random_bounds(self) -> None:
        """Created dragons can receive the minimum and maximum health."""
        with patch("dragon.dragon.randint", side_effect=[50, 100]):
            minimum_health_dragon = Dragon(name="Minimum")
            maximum_health_dragon = Dragon(name="Maximum")

        self.assertEqual(50, minimum_health_dragon.health)
        self.assertEqual(100, maximum_health_dragon.health)

    def test_scenario_health_cannot_be_supplied_by_the_caller(self) -> None:
        """The public constructor should not silently overwrite caller health."""
        with self.assertRaises(TypeError):
            Dragon(name="Wawelski", health=75)

    def test_scenario_invalid_name_and_initial_coordinates_are_rejected(
        self,
    ) -> None:
        """Public creation inputs use DragonError for invalid values."""
        scenarios = (
            {"name": None},
            {"name": True},
            {"name": "Wawelski", "position_x": False},
            {"name": "Wawelski", "position_y": 2.5},
        )

        for arguments in scenarios:
            with self.subTest(arguments=arguments):
                with self.assertRaises(DragonError):
                    Dragon(**arguments)


class DragonDamageBehaviorTestCase(TestCase):
    """Cover the Sprint 08 damage scenario."""

    def test_scenario_dragon_can_make_random_damage_between_five_and_twenty(
        self,
    ) -> None:
        """A named dragon should make damage between 5 and 20."""
        dragon = Dragon(name="Wawelski")

        damage = dragon.make_damage()

        self.assertGreaterEqual(damage, 5)
        self.assertLessEqual(damage, 20)


if __name__ == "__main__":
    main()
