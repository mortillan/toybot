from enum import Enum

class Direction(Enum):
  NORTH = 0
  EAST = 1
  WEST = 2
  SOUTH = 3

  def __str__(self):
    return ["NORTH", "EAST", "WEST", "SOUTH"][self.value]

def str_to_direction(str_direction):
  if str_direction == "NORTH":
    return Direction.NORTH
  elif str_direction == "SOUTH":
    return Direction.SOUTH
  elif str_direction == "EAST":
    return Direction.EAST
  elif str_direction == "WEST":
    return Direction.WEST
  else:
    raise Exception("Invalid value for direction")