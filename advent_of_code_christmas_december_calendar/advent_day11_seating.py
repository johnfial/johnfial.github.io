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
file_to_open = 'day11.txt'
with open(file_to_open, 'r') as file:
    navigation_raw = file.read()
navigation_list = navigation_raw.split('\n')

    # example:
example_navigation = '''F10
N3
F7
R90
F11'''
example_navigation = example_navigation.split('\n')


def part_one():
    # --- Part One: ---
    index = 0
    for number in years_as_list:
        # print(f'starting inner for loop for number {number} : ')    
        for number in years_as_list:
            # print(example_years_as_list[index] + number)
            if years_as_list[index] + number == 2020:
                print(f'found it! {years_as_list[index]} and {number}')            
                print(years_as_list[index] * number)
        index += 1


# part_one()
start_position = [0, 0, 90, ]
# North 000 / 360
# East 090
# South 180
# West 270

current_turn = 0
for turn in example_navigation:
    print(turn)
    current_turn += 1
    print(f'current turn is {current_turn} ')

    








def part_two():
    # --- Part Two: ---
    index_1 = 0
    for number in years_as_list:
        index_2 = 0
         
        for number in years_as_list:
            
            for number in years_as_list:

                if years_as_list[index_1] + years_as_list[index_2] + number == 2020:
                    print(f'found it! {years_as_list[index_1]} and {years_as_list[index_2]} and {number}')            
                    print(years_as_list[index_1] * years_as_list[index_2] * number)
            index_2 += 1

        index_1 += 1


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
