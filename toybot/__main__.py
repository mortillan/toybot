from toybot.simulator import Simulator
from toybot.toy_robot import ToyRobot
from toybot.direction import str_to_direction
from toybot.game import Game

def main():
  is_first_command = True

  toy_robot = ToyRobot()
  simulator = Simulator(toy_robot=toy_robot)

  g = Game(simulator=simulator)

  print("""
  ***********************************************************************************************************************************************************************************
  | Welcome to Toybot Simulator. This game lets you control a toyrobot in a 5 by 5 field.                                                                                           |
  | Below are the available commands to use. Type them correctly as commands are case sensitive.                                                                                    |
  |                                                                                                                                                                                 |
  | "PLACE X,Y,F" => Place the toy robot at index X,Y facing direction F. X and Y should be positive integer within the field and direction can only be NORTH, EAST, WEST, or SOUTH.|
  | "MOVE" => Move the toy robot 1 step facing the current direction, if the move makes it go out of the field, the command is ignored.                                             | 
  | "LEFT" => Turn the toy robot counter-clockwise.                                                                                                                                 |
  | "RIGHT" => Turn the toy robot clockwise.                                                                                                                                        |
  | "REPORT" => Outputs the current X,Y and direction of the toy robot.                                                                                                             |
  |                                                                                                                                                                                 |
  | Have fun =)                                                                                                                                                                     |
  | To quit press CTRL + C                                                                                                                                                          |
  ***********************************************************************************************************************************************************************************
  """)

  while True:
    command = input("Enter command: ")

    if command == "":
      continue
    
    tokens = command.split(" ")

    try:
      result = simulator.command(tokens)
      if result != None:
        print(result)
    except Exception as ex:
      print(ex)
    
if __name__ == "__main__":
  try:
    main()
  except KeyboardInterrupt:
      print("\n\nYou quit the game...Goodbye!")
      exit()