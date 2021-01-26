##############################################################################
# John Fial, PDX Code Guild, 2020-2021, www,johnfial.com
##############################################################################

# https://adventofcode.com/2020/day/1
# description pasted @ bottom

# cd C:\-=Cloud=-\Sync\git_working\weeks8-12_advent_christmas_december_calendar

import inspect
import itertools
def line_number():
    """Returns the current line number in our program."""
    return inspect.currentframe().f_back.f_lineno

    # REMEMBER TO : cd C:\-=Cloud=-\Sync\git_working\weeks8-12_advent_christmas_december_calendar
file_to_open = 'day01.txt'
with open(file_to_open, 'r') as file:
    years_raw = file.read()
years_as_list = years_raw.split('\n')
for i in range(0, len(years_as_list)):
    years_as_list[i] = int(years_as_list[i])

    # example:
example_raw = '''1543
1801
1731
1993
1496'''
example_years_as_list = example_raw.split('\n')
for i in range(0, len(example_years_as_list)):
    example_years_as_list[i] = int(example_years_as_list[i])

# print(len(example_years_as_list)) # main file is 200 lines

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

part_two()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# pasted from online:
    # import itertools

    # our_list = [1, 2, 3]

    # for L in range(0, len(our_list)+1):

    #     for subset in itertools.combinations(our_list, L):

    #         print(subset)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 


def old_attempt():

    # STEP 2 ADD TWO TOGETHER...
    attempts = 0
    index_a = 0
    index_b = 1

    while True:        

        if (years_as_list[index_a] + years_as_list[index_b]) == 2020:
            print(f'~~~~~~~~~~~~~~~worked with {years_as_list[index_a]} + {years_as_list[index_b]}!')
        else:
            # print(f'failed, added {years_as_list[index_a]} + {years_as_list[index_b]}, resulting in {years_as_list[index_a] + years_as_list[index_b]}.')
            # print('~')
            attempts += 1
            pass

        index_b += 1

        if attempts == 199:
            index_a = 1
            index_b = 1
            print(f'index_a {index_a} and index_b {index_b}.')
            print(f'attempts: {attempts}')
        
        if attempts == 398:
            # print(f'failed, added {years_as_list[index_a]} + {years_as_list[index_b]}, resulting in {years_as_list[index_a] + years_as_list[index_b]}.')
            print(f'index_a {index_a} and index_b {index_b}.')
            print(f'attempts: {attempts}')
            break

# print(len(years_as_list))
# old_attempt()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
print(f'|||| PROGRAM ENDED ||||.')




# STEP 3 IF A AND B = 2020, PRINT OUT ~~~HORRAY!~~~ OTHERWISE 'NOPE'
# --- Day 1: Report Repair ---

# After saving Christmas five years in a row, you've decided to take a vacation at a nice resort on a tropical island. Surely, Christmas will go on without you.

# The tropical island has its own currency and is entirely cash-only. The gold coins used there have a little picture of a starfish; the locals just call them stars. None of the currency exchanges seem to have heard of them, but somehow, you'll need to find fifty of these coins by the time you arrive so you can pay the deposit on your room.

# To save your vacation, you need to get all fifty stars by December 25th.

# Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

# Before you leave, the Elves in accounting just need you to fix your expense report (your puzzle input); apparently, something isn't quite adding up.

# Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.

# For example, suppose your expense report contained the following:

# 1721
# 979
# 366
# 299
# 675
# 1456

# In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.

# Of course, your expense report is much larger. Find the two entries that sum to 2020; what do you get if you multiply them together?
