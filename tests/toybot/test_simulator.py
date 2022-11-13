import unittest
from toybot.simulator import Simulator
from toybot.toy_robot import ToyRobot
from toybot.direction import Direction, str_to_direction

class TestSimulator(unittest.TestCase):
  def test_new_simulator_default(self):
    toy_robot = ToyRobot()
    s = Simulator(toy_robot=toy_robot)

    self.assertEqual(s.get_dimensions(), (5, 5))
  
  def test_new_simulator_with_dimension(self):
    dim = (10, 10)
    toy_robot = ToyRobot()
    s = Simulator(toy_robot=toy_robot, dimensions=dim)

    self.assertEqual(s.get_dimensions(), dim)

  def test_default_simulator_place_more_than_max_coordinate(self):
    toy_robot = ToyRobot()
    s = Simulator(toy_robot=toy_robot)

    with self.assertRaises(Exception):
      s.place(5, 0, Direction.SOUTH)
    with self.assertRaises(Exception):
      s.place(0, 5, Direction.SOUTH)
    with self.assertRaises(Exception):
      s.place(7, 7, Direction.SOUTH)

  def test_default_simulator_place_less_than_zero_coordinate(self):
    toy_robot = ToyRobot()
    s = Simulator(toy_robot=toy_robot)

    with self.assertRaises(Exception):
      s.place(-1, 0, Direction.SOUTH)
    with self.assertRaises(Exception):
      s.place(0, -1, Direction.SOUTH)   
    with self.assertRaises(Exception):     
      s.place(-10, -10, Direction.SOUTH)

  def test_default_move_north(self):
    toy_robot = ToyRobot()
    s = Simulator(toy_robot=toy_robot)

    s.move()

    self.assertEqual(s.get_toy_robot().x, 1)
    self.assertEqual(s.get_toy_robot().y, 0)
    self.assertEqual(s.get_toy_robot().f, Direction.NORTH)

  def test_move_north(self):
    toy_robot = ToyRobot()
    s = Simulator(toy_robot=toy_robot)

    pos_x = 1
    pos_y = 1
    direction = Direction.NORTH

    s.place(pos_x, pos_y, direction)
    s.move()

    self.assertEqual(s.get_toy_robot().x, pos_x + 1)
    self.assertEqual(s.get_toy_robot().y, pos_x)
    self.assertEqual(s.get_toy_robot().f, direction)

  def test_move_south(self):
    toy_robot = ToyRobot()
    s = Simulator(toy_robot=toy_robot)

    pos_x = 1
    pos_y = 1
    direction = Direction.SOUTH

    s.place(pos_x, pos_y, direction)
    s.move()

    self.assertEqual(s.get_toy_robot().x, pos_x - 1)
    self.assertEqual(s.get_toy_robot().y, pos_y)
    self.assertEqual(s.get_toy_robot().f, direction)

  def test_move_east(self):
    toy_robot = ToyRobot()
    s = Simulator(toy_robot=toy_robot)

    pos_x = 1
    pos_y = 1
    direction = Direction.EAST

    s.place(pos_x, pos_y, direction)
    s.move()

    self.assertEqual(s.get_toy_robot().x, pos_x)
    self.assertEqual(s.get_toy_robot().y, pos_y + 1)
    self.assertEqual(s.get_toy_robot().f, direction)

  def test_move_west(self):
    toy_robot = ToyRobot()
    s = Simulator(toy_robot=toy_robot)

    pos_x = 1
    pos_y = 1
    direction = Direction.WEST

    s.place(pos_x, pos_y, direction)
    s.move()

    self.assertEqual(s.get_toy_robot().x, pos_x)
    self.assertEqual(s.get_toy_robot().y, pos_y - 1)
    self.assertEqual(s.get_toy_robot().f, direction)

  def test_left_from_north(self):
    toy_robot = ToyRobot()
    s = Simulator(toy_robot=toy_robot)

    pos_x = 1
    pos_y = 1
    direction = Direction.NORTH

    s.place(pos_x, pos_y, direction)
    s.left()

    self.assertEqual(s.get_toy_robot().x, pos_x)
    self.assertEqual(s.get_toy_robot().y, pos_y)
    self.assertEqual(s.get_toy_robot().f, Direction.WEST)

  def test_left_from_east(self):
    toy_robot = ToyRobot()
    s = Simulator(toy_robot=toy_robot)

    pos_x = 1
    pos_y = 1
    direction = Direction.EAST

    s.place(pos_x, pos_y, direction)
    s.left()

    self.assertEqual(s.get_toy_robot().x, pos_x)
    self.assertEqual(s.get_toy_robot().y, pos_y)
    self.assertEqual(s.get_toy_robot().f, Direction.NORTH)

  def test_left_from_south(self):
    toy_robot = ToyRobot()
    s = Simulator(toy_robot=toy_robot)

    pos_x = 1
    pos_y = 1
    direction = Direction.SOUTH

    s.place(pos_x, pos_y, direction)
    s.left()

    self.assertEqual(s.get_toy_robot().x, pos_x)
    self.assertEqual(s.get_toy_robot().y, pos_y)
    self.assertEqual(s.get_toy_robot().f, Direction.EAST)

  def test_left_from_west(self):
    toy_robot = ToyRobot()
    s = Simulator(toy_robot=toy_robot)

    pos_x = 1
    pos_y = 1
    direction = Direction.WEST

    s.place(pos_x, pos_y, direction)
    s.left()

    self.assertEqual(s.get_toy_robot().x, pos_x)
    self.assertEqual(s.get_toy_robot().y, pos_y)
    self.assertEqual(s.get_toy_robot().f, Direction.SOUTH)

  def test_right_from_north(self):
    toy_robot = ToyRobot()
    s = Simulator(toy_robot=toy_robot)

    pos_x = 1
    pos_y = 1
    direction = Direction.NORTH

    s.place(pos_x, pos_y, direction)
    s.right()

    self.assertEqual(s.get_toy_robot().x, pos_x)
    self.assertEqual(s.get_toy_robot().y, pos_y)
    self.assertEqual(s.get_toy_robot().f, Direction.EAST)

  def test_right_from_east(self):
    toy_robot = ToyRobot()
    s = Simulator(toy_robot=toy_robot)

    pos_x = 1
    pos_y = 1
    direction = Direction.EAST

    s.place(pos_x, pos_y, direction)
    s.right()

    self.assertEqual(s.get_toy_robot().x, pos_x)
    self.assertEqual(s.get_toy_robot().y, pos_y)
    self.assertEqual(s.get_toy_robot().f, Direction.SOUTH)

  def test_right_from_south(self):
    toy_robot = ToyRobot()
    s = Simulator(toy_robot=toy_robot)

    pos_x = 1
    pos_y = 1
    direction = Direction.SOUTH

    s.place(pos_x, pos_y, direction)
    s.right()

    self.assertEqual(s.get_toy_robot().x, pos_x)
    self.assertEqual(s.get_toy_robot().y, pos_y)
    self.assertEqual(s.get_toy_robot().f, Direction.WEST)

  def test_right_from_west(self):
    toy_robot = ToyRobot()
    s = Simulator(toy_robot=toy_robot)

    pos_x = 1
    pos_y = 1
    direction = Direction.WEST

    s.place(pos_x, pos_y, direction)
    s.right()

    self.assertEqual(s.get_toy_robot().x, pos_x)
    self.assertEqual(s.get_toy_robot().y, pos_y)
    self.assertEqual(s.get_toy_robot().f, Direction.NORTH)

  def test_report_location(self):
    toy_robot = ToyRobot()
    s = Simulator(toy_robot=toy_robot)

    pos_x = 1
    pos_y = 1
    direction = Direction.WEST

    s.place(pos_x, pos_y, direction)
    
    self.assertEqual(s.report(), "OUTPUT: {},{},{}".format(pos_x, pos_y, direction))

    s.left()

    self.assertEqual(s.report(), "OUTPUT: {},{},{}".format(pos_x, pos_y, Direction.SOUTH))

    s.right()

    self.assertEqual(s.report(), "OUTPUT: {},{},{}".format(pos_x, pos_y, direction))
  
  def test_command_empty_string(self):
    toy_robot = ToyRobot()
    s = Simulator(toy_robot=toy_robot)

    with self.assertRaises(Exception):
      s.command("")
    s.command(["PLACE", "1,1,NORTH"])
    with self.assertRaises(Exception):
      s.command("")
    s.command(["REPORT"])

  def test_command_none_value(self):
    toy_robot = ToyRobot()
    s = Simulator(toy_robot=toy_robot)

    with self.assertRaises(Exception):
      s.command(None)
    s.command(["PLACE", "1,1,NORTH"])
    with self.assertRaises(Exception):
      s.command(None)
    s.command(["REPORT"])

  def test_command_empty_list(self):
    toy_robot = ToyRobot()
    s = Simulator(toy_robot=toy_robot)

    with self.assertRaises(Exception):
      s.command([])
    s.command(["PLACE", "1,1,NORTH"])
    with self.assertRaises(Exception):
      s.command([])
    s.command(["REPORT"])

  def test_command_list_empty_string_value(self):
    toy_robot = ToyRobot()
    s = Simulator(toy_robot=toy_robot)

    with self.assertRaises(Exception):
      s.command([""])
    s.command(["PLACE", "1,1,NORTH"])
    with self.assertRaises(Exception):
      s.command([""])
    s.command(["REPORT"])

  def test_place_non_positive_integer(self):
    toy_robot = ToyRobot()
    s = Simulator(toy_robot=toy_robot)

    s.place('1', '1', Direction.NORTH)

    with self.assertRaises(Exception):
      s.place('1.1', '0', Direction.NORTH)
    with self.assertRaises(Exception):
      s.place('0', '1.1', Direction.NORTH)
    with self.assertRaises(Exception):
      s.place('1.1', '1.1', Direction.NORTH)

  def test_command_invalid_place_command(self):
    toy_robot = ToyRobot()
    s = Simulator(toy_robot=toy_robot)

    s.command(["PLACE", "1,1,NORTH"])
    self.assertEqual(s.command(["REPORT"]), "OUTPUT: {},{},{}".format(1, 1, "NORTH"))

    with self.assertRaises(Exception):
      s.command(["PLACE"])
    with self.assertRaises(Exception):
      s.command(["PLACE", ""])
    with self.assertRaises(Exception):
      s.command(["PLACE", None])
    with self.assertRaises(Exception):
      s.command(["PLACE", []])
    with self.assertRaises(Exception):
      s.command(["PLACE", "2.0,1,SOUTH"])
    with self.assertRaises(Exception):
      s.command(["", "PLACE"])
    with self.assertRaises(Exception):
      s.command(["PLACE", ",,"])
    with self.assertRaises(Exception):
      s.command(["PLACE", ","])
    
    s.command(["PLACE", "0,0,SOUTH"])
    self.assertEqual(s.command(["REPORT"]), "OUTPUT: {},{},{}".format(0, 0, "SOUTH"))
  
  def test_command_place_wrong_parameters(self):
    toy_robot = ToyRobot()
    s = Simulator(toy_robot=toy_robot)

    with self.assertRaises(Exception):
      s.command(["PLACE", "1,1"])
    with self.assertRaises(Exception):
      s.command(["PLACE", "1,1,2,SOUTH"])
    with self.assertRaises(Exception):
      s.command(["PLACE", "1"])
    with self.assertRaises(Exception):
      s.command(["PLACE", "1,SOUTH"])

  def test_command_move_parameters_should_be_ignored(self):
    toy_robot = ToyRobot()
    s = Simulator(toy_robot=toy_robot)

    s.command(["PLACE", "0,1,NORTH"])
    s.command(["MOVE"])
    self.assertEqual(s.command(["REPORT"]), "OUTPUT: {},{},{}".format(1, 1, "NORTH"))
    s.command(["MOVE", ""])
    self.assertEqual(s.command(["REPORT"]), "OUTPUT: {},{},{}".format(2, 1, "NORTH"))
    s.command(["MOVE", None])
    self.assertEqual(s.command(["REPORT"]), "OUTPUT: {},{},{}".format(3, 1, "NORTH"))
    s.command(["MOVE", []])
    self.assertEqual(s.command(["REPORT"]), "OUTPUT: {},{},{}".format(4, 1, "NORTH"))

  def test_command_left(self):
    toy_robot = ToyRobot()
    s = Simulator(toy_robot=toy_robot)

    s.command(["PLACE", "0,0,NORTH"])

    self.assertEqual(s.command(["REPORT"]), "OUTPUT: {},{},{}".format(0, 0, "NORTH"))

    s.command(["LEFT"])

    self.assertEqual(s.command(["REPORT"]), "OUTPUT: {},{},{}".format(0, 0, "WEST"))
  
  def test_command_right(self):
    toy_robot = ToyRobot()
    s = Simulator(toy_robot=toy_robot)

    s.command(["PLACE", "0,0,NORTH"])

    self.assertEqual(s.command(["REPORT"]), "OUTPUT: {},{},{}".format(0, 0, "NORTH"))

    s.command(["RIGHT"])

    self.assertEqual(s.command(["REPORT"]), "OUTPUT: {},{},{}".format(0, 0, "EAST"))