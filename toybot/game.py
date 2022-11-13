from toybot.simulator import Simulator
from toybot.toy_robot import ToyRobot
from toybot.direction import str_to_direction

class Game:
  def __init__(self, simulator):
    self.__simulator = simulator

  