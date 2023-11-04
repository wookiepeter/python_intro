import sys
import math

# complete solution for this puzzle: https://www.codingame.com/ide/puzzle/power-of-thor-episode-1

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

thor_x = initial_tx
thor_y = initial_ty

# game loop
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)


    # A single line providing the move to be made: N NE E SE S SW W or NW
    result = ""
    # handle vertical movement
    if thor_y < light_y: 
        result += "S"
        thor_y = thor_y + 1
    elif thor_y > light_y:  
        result += "N"
        thor_y = thor_y - 1
    # handle horizontal movement
    if thor_x > light_x: 
        result += "W"
        thor_x = thor_x - 1
    elif thor_x < light_x: 
        result += "E"
        thor_x = thor_x + 1
    print(result)