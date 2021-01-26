##############################################################################
# John Fial, PDX Code Guild, 2020-2021, www,johnfial.com
##############################################################################

# https://adventofcode.com/2020/day/1
# description pasted @ bottom

# cd C:\-=Cloud=-\Sync\git_working\weeks8-12_advent_christmas_december_calendar
# https://adventofcode.com/2020/day/12

import inspect
import itertools

def line_number():
    """Returns the current line number in our program."""
    return inspect.currentframe().f_back.f_lineno

    # REMEMBER TO : cd C:\-=Cloud=-\Sync\git_working\weeks8-12_advent_christmas_december_calendar
file_to_open = 'day12.txt'
with open(file_to_open, 'r') as file:
    navigation_raw = file.read()

    # examples:
example_navigation = '''F10
N3
F7
R90
F11'''
example_navigation2 = '''F77
E4
S2
W1
L180
N4
R180
S3
W5
F86
L90
E1
F16
R90
N1
E1
F86
S1
F36
E2
L180
N5
F46
N1
L90
F43
S5
R90
F41'''

# print(type(navigation_list))
# print(len(navigation_list))

def part_one(input_data):

    start_position = [0, 0, 90, ] # [+N/-S, +E/-W, bearing]
    current_position = start_position

    input_data = input_data.split('\n')

    # North 000 / 360, [0] positive
    # East 090 [1] positive
    # South 180 [0] negative
    # West 270 [1] negative

    current_turn = 1
    valid_bearings = [0, 90, 180, 270, 360]
    for turn in input_data: 
        print(f'------------------turn: {current_turn}--------------------')
        print(f'start position: N/S: {current_position[0]}. E/W: {current_position[1]}. Bearing: {current_position[2]}. nav: ((( {turn} ))).')
        
        # move: current_position[1] += 1
        
        # forward movement:
        if turn[0] == 'F':
            change = int(turn[1:4])
            print(f'moving forward! by {change}')

            if current_position[2] == 90: # east +
                current_position[1] += change
            elif current_position[2] == 270: # west -
                current_position[1] -= change

            elif current_position[2] == 0: # north +
                current_position[0] += change
            elif current_position[2] == 180: # south -
                current_position[0] -= change
        
        # four directions
        elif turn[0] == 'N':
            print(f'moving north! by {turn[1:4]}')
            change = int(turn[1:4])
            current_position[0] += change
        elif turn[0] == 'S':
            print(f'moving south! by {turn[1:4]}')
            change = int(turn[1:4])
            current_position[0] -= change
        elif turn[0] == 'E':
            print(f'moving east! by {turn[1:4]}')
            change = int(turn[1:4])
            current_position[1] += change
        elif turn[0] == 'W':
            print(f'moving west! by {turn[1:4]}')
            change = int(turn[1:4])
            current_position[1] -= change
        
        # turn bearing
        elif turn[0] == 'L':
            change = int(turn[1:4])
            print(f'turning by - {change}')
            current_position[2] -= change
        elif turn[0] == 'R':
            change = int(turn[1:4])
            print(f'turning by + {change}')
            current_position[2] += change

        # fix issues with bearing outside cardinal possibilities: 0, 90, 180, and 270: 
        if int(current_position[2]) == -90: # west reset
            current_position[2] = 270 # west
        if int(current_position[2]) == -180: # south reset
            current_position[2] = 180 # south
        if int(current_position[2]) == -270: # east reset
            current_position[2] = 90 # east
        
        
        if int(current_position[2]) == 360: # north reset
            current_position[2] = 0 # north
        if int(current_position[2]) == 450: # east reset
            current_position[2] = 90 # east
        if int(current_position[2]) == 540: # south reset
            current_position[2] = 180 # south
        
        # trick: a left 270 turn is = a right 90 turn!
            #   0-270 = 90
            # 90-270 = 180
            # 180-270 = 270

        # ... so a right 270 turn is = a left 90 turn! 

        
        if int(current_position[2]) not in valid_bearings:
            print('~ ~ ~ ~ ~ ~ ~ ~ ~ ~ alert!!!!!!!!!!! ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ')

        print(f'  end position: N/S: {current_position[0]}. E/W: {current_position[1]}. Bearing: {current_position[2]}.')
        current_turn += 1

    return current_position

# print(part_one(navigation_raw)) # actual data file
# print(part_one(example_navigation2))


def part_two(input_data):

    ship_start_position = [0, 0, 90, ]
    current_position = ship_start_position
    input_data = input_data.split('\n')
    current_instruction_line = 1
    valid_bearings = [0, 90, 180, 270, 360]

    waypoint_relative = []
    waypoint_relative = [1, 10, 0, ] # remember i have N/S first, then E/W, then a bearing, which should always be empty...

    # turn should be renamed 'instruction' for part 2...
    for turn in input_data: 
        print(f'------------------turn: {current_instruction_line}--------------------')
        print(f'start position: N/S: {current_position[0]}. E/W: {current_position[1]}. Bearing: {current_position[2]}. nav: ((( {turn} ))).')
                







    # ------------------------------------------------------------------------------
    # SHIP MOVEMENT SECTION
    # section done, i think?
        if turn[0] == 'F':
        # Action F means to move forward to the waypoint a number of times equal to the given value.,         # F moves the current position ONCE for each 'F' number
           
            number_of_times_to_hop_to_waypoint = int(turn[1:4])

            print(f'moving to waypoint {number_of_times_to_hop_to_waypoint} times...')
            for hop in range(0, number_of_times_to_hop_to_waypoint):
                current_position[0] += waypoint_relative[0] # hops north or south based on waypoint
                current_position[1] += waypoint_relative[1] # hops east or west based on waypoint

                # if current_position[2] == 90: # east +
                #     current_position[1] += change
                # elif current_position[2] == 270: # west -
                #     current_position[1] -= change

                # elif current_position[2] == 0: # north +
                #     current_position[0] += change
                # elif current_position[2] == 180: # south -
                #     current_position[0] -= change









    # ------------------------------------------------------------------------------
    # CHANGE WAYPOINT SECTION
        
        # The waypoint starts 10 units east and 1 unit north relative to the ship. The waypoint is relative to the ship; that is, if the ship moves, the waypoint moves with it.
        # Almost all of the actions indicate how to move a waypoint which is relative to the ship's position:
        # MOVE THE WAYPOINT NOW, NOT THE BOAT
        elif turn[0] == 'N':
            print(f'changing waypoint_relative by {turn[1:4]}')
            change = int(turn[1:4])
            waypoint_relative[0] += change
        elif turn[0] == 'S':
            print(f'changing waypoint_relative by {turn[1:4]}')
            change = int(turn[1:4])
            waypoint_relative[0] -= change
        elif turn[0] == 'E':
            print(f'changing waypoint_relative by {turn[1:4]}')
            change = int(turn[1:4])
            waypoint_relative[1] += change
        elif turn[0] == 'W':
            print(f'changing waypoint_relative by {turn[1:4]}')
            change = int(turn[1:4])
            waypoint_relative[1] -= change

    # ------------------------------------------------------------------------------









    # ------------------------------------------------------------------------------
    # ! ROTATE ! WAYPOINT ! SECTION !
    # changing the waypoint is going to be the most difficult, rotating the entire thing...
        
    #     Action L means to rotate the waypoint around the ship left (counter-clockwise) the given number of degrees.
    #     Action R means to rotate the waypoint around the ship right (clockwise) the given number of degrees.
        # turn bearing
        elif turn[0] == 'L':
            # change = int(turn[1:4])
            print(f'rotating waypoint_relative.....')
            # current_position[2] -= change
        elif turn[0] == 'R':
            # change = int(turn[1:4])
            print(f'rotating waypoint_relative.....')
            # current_position[2] += change

        if int(current_position[2]) == -90: # west reset
            current_position[2] = 270 # west
        if int(current_position[2]) == -180: # south reset
            current_position[2] = 180 # south
        if int(current_position[2]) == -270: # east reset
            current_position[2] = 90 # east        
        
        if int(current_position[2]) == 360: # north reset
            current_position[2] = 0 # north
        if int(current_position[2]) == 450: # east reset
            current_position[2] = 90 # east
        if int(current_position[2]) == 540: # south reset
            current_position[2] = 180 # south
        
        # trick: a left 270 turn is = a right 90 turn!
            #   0-270 = 90
            # 90-270 = 180
            # 180-270 = 270
        # ... so a right 270 turn is = a left 90 turn! 
        
        if int(current_position[2]) not in valid_bearings:
            print('~ ~ ~ ~ ~ ~ ~ ~ ~ ~ alert!!!!!!!!!!! ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ')

    # END section rotating waypoint axis
    # ------------------------------------------------------------------------------






    # ------------------------------------------------------------------------------

        print(f'  end position: N/S: {current_position[0]}. E/W: {current_position[1]}. Bearing: {current_position[2]}.')
        current_instruction_line += 1
    return current_position


# print(part_two(example_navigation2))
# print(part_two(navigation_raw)) # actual data file
print(part_two(example_navigation))
#     --- Part Two ---
# For example, using the same instructions as above:
#     F10 moves the ship to the waypoint 10 times (a total of 100 units east and 10 units north), leaving the ship at east 100, north 10. The waypoint stays 10 units east and 1 unit north of the ship.
#     N3 moves the waypoint 3 units north to 10 units east and 4 units north of the ship. The ship remains at east 100, north 10.
#     F7 moves the ship to the waypoint 7 times (a total of 70 units east and 28 units north), leaving the ship at east 170, north 38. The waypoint stays 10 units east and 4 units north of the ship.
#     R90 rotates the waypoint around the ship clockwise 90 degrees, moving it to 4 units east and 10 units south of the ship. The ship remains at east 170, north 38.
#     F11 moves the ship to the waypoint 11 times (a total of 44 units east and 110 units south), leaving the ship at east 214, south 72. The waypoint stays 4 units east and 10 units south of the ship.
# After these operations, the ship's Manhattan distance from its starting position is 214 + 72 = 286.





# def part_two():
#     # --- Part Two: ---
#     index_1 = 0
#     for number in years_as_list:
#         index_2 = 0
         
#         for number in years_as_list:
            
#             for number in years_as_list:

#                 if years_as_list[index_1] + years_as_list[index_2] + number == 2020:
#                     print(f'found it! {years_as_list[index_1]} and {years_as_list[index_2]} and {number}')            
#                     print(years_as_list[index_1] * years_as_list[index_2] * number)
#             index_2 += 1

#         index_1 += 1


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
print(f'|||| PROGRAM ENDED ||||.')




# --- Day 12: Rain Risk ---

# Your ferry made decent progress toward the island, but the storm came in faster than anyone expected. The ferry needs to take evasive actions!

# Unfortunately, the ship's navigation computer seems to be malfunctioning; rather than giving a route directly to safety, it produced extremely circuitous instructions. When the captain uses the PA system to ask if anyone can help, you quickly volunteer.

# The navigation instructions (your puzzle input) consists of a sequence of single-character actions paired with integer input values. After staring at them for a few minutes, you work out what they probably mean:

#     Action N means to move north by the given value.
#     Action S means to move south by the given value.
#     Action E means to move east by the given value.
#     Action W means to move west by the given value.
#     Action L means to turn left the given number of degrees.
#     Action R means to turn right the given number of degrees.
#     Action F means to move forward by the given value in the direction the ship is currently facing.

# The ship starts by facing east. Only the L and R actions change the direction the ship is facing. (That is, if the ship is facing east and the next instruction is N10, the ship would move north 10 units, but would still move east if the following action were F.)

# For example:

# F10
# N3
# F7
# R90
# F11

# These instructions would be handled as follows:

#     F10 would move the ship 10 units east (because the ship starts by facing east) to east 10, north 0.
#     N3 would move the ship 3 units north to east 10, north 3.
#     F7 would move the ship another 7 units east (because the ship is still facing east) to east 17, north 3.
#     R90 would cause the ship to turn right by 90 degrees and face south; it remains at east 17, north 3.
#     F11 would move the ship 11 units south to east 17, south 8.

# At the end of these instructions, the ship's Manhattan distance (sum of the absolute values of its east/west position and its north/south position) from its starting position is 17 + 8 = 25.

# Figure out where the navigation instructions lead. What is the Manhattan distance between that location and the ship's starting position?
