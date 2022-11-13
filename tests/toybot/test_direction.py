import unittest
from toybot.direction import str_to_direction, Direction

class TestDirection(unittest.TestCase):
  def test_str_to_direction_with_valid_values(self):
    self.assertEqual(str_to_direction("NORTH"), Direction.NORTH)
    self.assertEqual(str_to_direction("EAST"), Direction.EAST)
    self.assertEqual(str_to_direction("WEST"), Direction.WEST)
    self.assertEqual(str_to_direction("SOUTH"), Direction.SOUTH)
  
  def test_str_to_direction_with_north_string(self):
    with self.assertRaises(Exception):
      str_to_direction("ANYTHING")