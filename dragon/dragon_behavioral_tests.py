"""Behavioral acceptance tests for the Dragon project."""

from unittest import TestCase, main

from dragon import Dragon


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

    def test_use_case_movement_sequence(self) -> None:
        """The Sprint 07 use case ends at position (20, 40)."""
        dragon = Dragon(name="Wawelski")
        self.assertEqual("(50, 100)", dragon.get_position())

        dragon.set_position(position_x=10, position_y=20)
        dragon.move_left(10)
        dragon.move_down(20)
        dragon.move_left(10)
        dragon.move_right(15)
        dragon.move_right(15)
        dragon.move_up(5)
        dragon.move_down(5)

        self._then_position_is(dragon, position_x=20, position_y=40)


if __name__ == "__main__":
    main()
