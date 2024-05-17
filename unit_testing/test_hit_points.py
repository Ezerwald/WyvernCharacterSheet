import unittest
from unittest.mock import MagicMock
from health import HitPoints
from abstract_character import AbstractCharacter
from game_classes import GameClass
from character_stats import Level


class TestHitPoints(unittest.TestCase):
    def setUp(self):
        self.mock_character = MagicMock(spec=AbstractCharacter)
        self.mock_character.current_game_class = MagicMock(spec=GameClass)
        self.mock_character.current_game_class.value.hit_dice_type = 8
        self.mock_character.level = MagicMock(spec=Level)
        self.mock_character.level.value = 5

        self.hit_points = HitPoints(self.mock_character)

    def test_initialization(self):
        self.assertEqual(self.hit_points.current_hit_points, self.hit_points.max_hit_points)

    def test_set_current_hit_points(self):
        self.hit_points.current_hit_points = 20
        self.assertEqual(self.hit_points.current_hit_points, 20)

    def test_set_max_hit_points(self):
        self.hit_points.max_hit_points = 50
        self.assertEqual(self.hit_points.max_hit_points, 50)

    def test_current_hit_points_cannot_be_negative(self):
        with self.assertRaises(ValueError):
            self.hit_points.current_hit_points = -10

    def test_max_hit_points_cannot_be_negative(self):
        with self.assertRaises(ValueError):
            self.hit_points.max_hit_points = -10

    def test_max_hit_points_adjustment(self):
        self.hit_points.max_hit_points = 20
        self.assertEqual(self.hit_points.current_hit_points, 20)


if __name__ == "__main__":
    unittest.main()
