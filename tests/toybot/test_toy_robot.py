import unittest

from toybot.toy_robot import ToyRobot, Direction

class TestToyRobot(unittest.TestCase):
  def test_new_toy_robot(self):
    toy_robot = ToyRobot()

    self.assertEqual(toy_robot.x, 0)
    self.assertEqual(toy_robot.y, 0)
    self.assertEqual(toy_robot.f, Direction.NORTH)

  def test_move_robot(self):
    toy_robot = ToyRobot()

    toy_robot.move(2, 3, Direction.EAST)

    self.assertEqual(toy_robot.x, 2)
    self.assertEqual(toy_robot.y, 3)
    self.assertEqual(toy_robot.f, Direction.EAST)
