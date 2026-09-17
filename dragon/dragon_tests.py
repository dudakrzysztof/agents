"""Tests for the dragon project."""

from inspect import signature
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

    def test_create_dragon_with_non_string_name_raises_dragon_error(self) -> None:
        """Names of every non-string type should be rejected consistently."""
        for invalid_name in (None, 1, True, 1.5, ["Wawelski"]):
            with self.subTest(invalid_name=invalid_name):
                with self.assertRaisesRegex(
                    DragonError, "^Dragon name must be a string$"
                ):
                    Dragon(name=invalid_name)


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
        generated_health = list(range(50, 60))
        with patch(
            "dragon.dragon.randint", side_effect=generated_health
        ) as randint_mock:
            dragons = [
                Dragon(name=f"Dragon{dragon_index}")
                for dragon_index in range(10)
            ]
        health_values = [dragon.health for dragon in dragons]

        self.assertEqual(generated_health, health_values)
        self.assertEqual([call(50, 100)] * 10, randint_mock.call_args_list)

    def test_dragon_health_can_be_generated_at_inclusive_bounds(self) -> None:
        """Health generation should permit both 50 and 100."""
        with patch("dragon.dragon.randint", side_effect=[50, 100]):
            minimum_health_dragon = Dragon(name="Minimum")
            maximum_health_dragon = Dragon(name="Maximum")

        self.assertEqual(50, minimum_health_dragon.health)
        self.assertEqual(100, maximum_health_dragon.health)

    def test_health_is_not_a_public_constructor_parameter(self) -> None:
        """Callers should not be offered an ignored health argument."""
        self.assertNotIn("health", signature(Dragon).parameters)

        with self.assertRaises(TypeError):
            Dragon(name="Wawelski", health=75)


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

    def test_dragon_can_be_created_at_negative_coordinates(self) -> None:
        """Signed integer coordinates should be accepted at creation."""
        dragon = Dragon(name="Wawelski", position_x=-50, position_y=-100)

        self.assertEqual((-50, -100), dragon.position)

    def test_initial_coordinates_reject_non_integers_and_booleans(self) -> None:
        """Both constructor coordinates should require non-boolean integers."""
        invalid_values = (True, False, None, 1.5, "1", [1])

        for parameter_name in ("position_x", "position_y"):
            for invalid_value in invalid_values:
                with self.subTest(
                    parameter_name=parameter_name,
                    invalid_value=invalid_value,
                ):
                    arguments = {parameter_name: invalid_value}
                    with self.assertRaisesRegex(
                        DragonError,
                        rf"^{parameter_name} must be an integer$",
                    ):
                        Dragon(name="Wawelski", **arguments)

    def test_dragon_returns_current_position(self) -> None:
        """A dragon should return its current position in coordinate format."""
        dragon = Dragon(name="Wawelski")
        dragon.position_x = 1
        dragon.position_y = 2

        self.assertEqual("(1, 2)", dragon.get_position())

    def test_position_property_returns_coordinate_tuple(self) -> None:
        """The position property should expose both coordinates as a tuple."""
        dragon = Dragon(name="Wawelski", position_x=-1, position_y=2)

        self.assertEqual((-1, 2), dragon.position)
        self.assertIsInstance(dragon.position, tuple)
        self.assertEqual("(-1, 2)", dragon.get_position())

    def test_position_property_is_read_only(self) -> None:
        """Assigning to the combined position property should be prohibited."""
        dragon = Dragon(name="Wawelski", position_x=1, position_y=2)

        with self.assertRaises(AttributeError):
            dragon.position = (3, 4)

        self.assertEqual((1, 2), dragon.position)

    def test_dragon_can_be_set_at_any_position(self) -> None:
        """A dragon should move to the position provided by the caller."""
        dragon = Dragon(name="Wawelski")

        dragon.set_position(position_x=1, position_y=2)

        self.assertEqual(1, dragon.position_x)
        self.assertEqual(2, dragon.position_y)

    def test_set_position_accepts_negative_coordinates(self) -> None:
        """Absolute coordinates may be signed integers."""
        dragon = Dragon(name="Wawelski")

        dragon.set_position(position_x=-1, position_y=-2)

        self.assertEqual((-1, -2), dragon.position)

    def test_set_position_is_atomic_when_an_input_is_invalid(self) -> None:
        """Invalid coordinates should never cause a partial position update."""
        invalid_values = (True, False, None, 1.5, "1", [1])

        for parameter_name in ("position_x", "position_y"):
            for invalid_value in invalid_values:
                with self.subTest(
                    parameter_name=parameter_name,
                    invalid_value=invalid_value,
                ):
                    dragon = Dragon(
                        name="Wawelski", position_x=10, position_y=20
                    )
                    arguments = {"position_x": 30, "position_y": 40}
                    arguments[parameter_name] = invalid_value

                    with self.assertRaisesRegex(
                        DragonError,
                        rf"^{parameter_name} must be an integer$",
                    ):
                        dragon.set_position(**arguments)

                    self.assertEqual((10, 20), dragon.position)

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

    def test_move_accepts_signed_integer_offsets(self) -> None:
        """Positive and negative offsets should both be applied."""
        dragon = Dragon(name="Wawelski", position_x=-10, position_y=-20)

        dragon.move(x=-5, y=7)

        self.assertEqual((-15, -13), dragon.position)

    def test_move_rejects_invalid_offsets_without_mutating_position(self) -> None:
        """Combined movement should validate both offsets before moving."""
        invalid_values = (True, False, None, 1.5, "1", [1])

        for parameter_name in ("x", "y"):
            for invalid_value in invalid_values:
                with self.subTest(
                    parameter_name=parameter_name,
                    invalid_value=invalid_value,
                ):
                    dragon = Dragon(
                        name="Wawelski", position_x=10, position_y=20
                    )
                    arguments = {"x": 30, "y": 40}
                    arguments[parameter_name] = invalid_value

                    with self.assertRaisesRegex(
                        DragonError,
                        rf"^{parameter_name} must be an integer$",
                    ):
                        dragon.move(**arguments)

                    self.assertEqual((10, 20), dragon.position)

    def test_directional_methods_reject_non_integers_and_booleans(self) -> None:
        """Each directional movement should validate its public offset."""
        invalid_values = (True, False, None, 1.5, "1", [1])

        for method_name in (
            "move_right",
            "move_left",
            "move_down",
            "move_up",
        ):
            for invalid_value in invalid_values:
                with self.subTest(
                    method_name=method_name,
                    invalid_value=invalid_value,
                ):
                    dragon = Dragon(
                        name="Wawelski", position_x=10, position_y=20
                    )

                    with self.assertRaisesRegex(
                        DragonError, "^value must be an integer$"
                    ):
                        getattr(dragon, method_name)(invalid_value)

                    self.assertEqual((10, 20), dragon.position)

    def test_directional_methods_accept_signed_integer_offsets(self) -> None:
        """Negative values should retain directional arithmetic behavior."""
        scenarios = (
            ("move_right", (7, 20)),
            ("move_left", (13, 20)),
            ("move_down", (10, 17)),
            ("move_up", (10, 23)),
        )

        for method_name, expected_position in scenarios:
            with self.subTest(method_name=method_name):
                dragon = Dragon(
                    name="Wawelski", position_x=10, position_y=20
                )

                getattr(dragon, method_name)(-3)

                self.assertEqual(expected_position, dragon.position)

    def test_directional_methods_delegate_to_combined_move(self) -> None:
        """Single-direction helpers should use the combined movement path."""
        dragon = Dragon(name="Wawelski")

        with patch.object(Dragon, "move", autospec=True) as move_mock:
            dragon.move_right(1)
            dragon.move_left(2)
            dragon.move_down(3)
            dragon.move_up(4)

        self.assertEqual(
            [
                call(dragon, x=1),
                call(dragon, x=-2),
                call(dragon, y=3),
                call(dragon, y=-4),
            ],
            move_mock.call_args_list,
        )


if __name__ == "__main__":
    main()
