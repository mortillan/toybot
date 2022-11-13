from toybot.direction import Direction, str_to_direction

class Simulator:
  def __init__(self, toy_robot, dimensions = None):
    self.__dimensions = dimensions if dimensions is not None else (5, 5)
    self.__toy_bot = toy_robot
    self.__is_first_command = True

  def get_dimensions(self):
    return self.__dimensions

  def get_toy_robot(self):
    return self.__toy_bot

  def __is_out_of_bounds(self, x, y, f):
    if x >= self.__dimensions[0] or x < 0 or y >= self.__dimensions[1] or y < 0:
      return True
    
    return False

  def place(self, x, y, f):
    try:
      x = int(x)
      y = int(y)
    except ValueError:
      raise Exception("coordinates are not valid integers")
    
    if self.__is_out_of_bounds(x, y , f):
      raise Exception("coordinates x = {}, y = {} is out of bounds in {},{} field".format(x, y, self.__dimensions[0], self.__dimensions[1]))
    
    self.__toy_bot.move(x, y, f)

  # Moves the robot 1 step forward on the direction it is facing
  def move(self):
    if self.__toy_bot.f == Direction.NORTH:
      self.place(self.__toy_bot.x + 1, self.__toy_bot.y, self.__toy_bot.f)
    elif self.__toy_bot.f == Direction.SOUTH:
      self.place(self.__toy_bot.x - 1, self.__toy_bot.y, self.__toy_bot.f)
    elif self.__toy_bot.f == Direction.EAST:
      self.place(self.__toy_bot.x, self.__toy_bot.y + 1, self.__toy_bot.f)
    else:
      self.place(self.__toy_bot.x, self.__toy_bot.y - 1, self.__toy_bot.f)

  # Change the direction the robot is facing counter clockwise
  def left(self):
    if self.__toy_bot.f == Direction.NORTH:
      # robot is facing north, change facing to west
      self.place(self.__toy_bot.x, self.__toy_bot.y, Direction.WEST)
    elif self.__toy_bot.f == Direction.SOUTH:
      # robot is facing south, change facing to east
      self.place(self.__toy_bot.x, self.__toy_bot.y, Direction.EAST)
    elif self.__toy_bot.f == Direction.EAST:
      # robot is facing east, change facing to north
      self.place(self.__toy_bot.x, self.__toy_bot.y, Direction.NORTH)
    else:
      # robot is facing west, change facing to south
      self.place(self.__toy_bot.x, self.__toy_bot.y, Direction.SOUTH)

  # Change the direction the robot is facing clockwise
  def right(self):
    if self.__toy_bot.f == Direction.NORTH:
      # robot is facing north, change facing to east
      self.place(self.__toy_bot.x, self.__toy_bot.y, Direction.EAST)
    elif self.__toy_bot.f == Direction.SOUTH:
      # robot is facing south, change facing to west
      self.place(self.__toy_bot.x, self.__toy_bot.y, Direction.WEST)
    elif self.__toy_bot.f == Direction.EAST:
      # robot is facing east, change facing to south
      self.place(self.__toy_bot.x, self.__toy_bot.y, Direction.SOUTH)
    else:
      # robot is facing west, change facing to north
      self.place(self.__toy_bot.x, self.__toy_bot.y, Direction.NORTH)
  
  def report(self):
    return "OUTPUT: {},{},{}".format(self.__toy_bot.x, self.__toy_bot.y, str(self.__toy_bot.f))

  def command(self, tokens):
    if type(tokens) != list or tokens == None or tokens == "" or len(tokens) == 0:
      raise Exception("Invalid command")
    
    command = tokens[0] if len(tokens) > 0 else None
    param = tokens[1] if len(tokens) > 1 else None
    
    if self.__is_first_command and command != "PLACE":
      raise Exception("PLACE command must be the first command to execute")

    if command == "PLACE" and param != None:
      place_cmd = param.split(",")
      
      if len(place_cmd) != 3:
        raise Exception("invalid format to coordinates and direction for PLACE command")

      direction = str_to_direction(place_cmd[2])
      self.place(place_cmd[0], place_cmd[1], direction)

      self.__is_first_command = False
      return
    elif command == "MOVE":
      return self.move()
    elif command == "LEFT":
      return self.left()
    elif command == "RIGHT":
      return self.right()
    elif command == "REPORT":
      return self.report()
    else:
      raise Exception("Invalid command")