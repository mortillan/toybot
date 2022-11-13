from toybot.direction import Direction

class ToyRobot:
  def __init__(self):
    self.x = 0
    self.y = 0
    self.f = Direction.NORTH

  def move(self, x, y, f):
    self.x = x
    self.y = y
    self.f = f