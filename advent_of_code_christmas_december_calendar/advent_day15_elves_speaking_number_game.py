##############################################################################
# John Fial, PDX Code Guild, 2020-2021, www,johnfial.com
##############################################################################

# https://adventofcode.com/2020/day/1
# description pasted @ bottom

# cd C:\-=Cloud=-\Sync\git_working\weeks8-12_advent_christmas_december_calendar
# https://adventofcode.com/2020/day/15

import inspect

def line_number():
    """Returns the current line number in our program."""
    return inspect.currentframe().f_back.f_lineno

# REMEMBER TO : cd C:\-=Cloud=-\Sync\git_working\weeks8-12_advent_christmas_december_calendar


##############################################################################
    # # # # Then, each turn consists of considering the most recently spoken number:# # # # 

    # For example, suppose the starting numbers are 0,3,6:
    #     Turn 1: The 1st number spoken is a starting number, 0.
    #     Turn 2: The 2nd number spoken is a starting number, 3.
    #     Turn 3: The 3rd number spoken is a starting number, 6.

    #     Turn 4: Now, consider the last number spoken, 6. Since that was the first time the number had been spoken, 
    #       the 4th number spoken is 0.
    #     Turn 5: Next, again consider the last number spoken, 0. Since it had been spoken before, 
    #       the next number to speak is the difference between the turn number when it was 
    #       last spoken (the previous turn, 4) and the turn number of the time it was most recently spoken 
    #       before then (turn 1). Thus, the 5th number spoken is 4 - 1, 3.
    #     Turn 6: The last number spoken, 3 had also been spoken before, most recently on turns 5 and 2. 
    #       So, the 6th number spoken is 5 - 2, 3.
    #     Turn 7: Since 3 was just spoken twice in a row, and the last two turns are 1 turn apart, 
    #       the 7th number spoken is 1.
    #     Turn 8: Since 1 is new, the 8th number spoken is 0.
    #     Turn 9: 0 was last spoken on turns 8 and 4, so the 9th number spoken is the difference between them, 4.
    #     Turn 10: 4 is new, so the 10th number spoken is 0.
    # Their question for you is: what will be the 2020th number spoken? In the example above, 
        # the 2020th number spoken will be 436.
                # examples:
                # Here are a few more examples:
                #     Given the starting numbers 1,3,2, the 2020th number spoken is 1.
                #     Given the starting numbers 2,1,3, the 2020th number spoken is 10.
                #     Given the starting numbers 1,2,3, the 2020th number spoken is 27.
                #     Given the starting numbers 2,3,1, the 2020th number spoken is 78.
                #     Given the starting numbers 3,2,1, the 2020th number spoken is 438.
                #     Given the starting numbers 3,1,2, the 2020th number spoken is 1836.

def part_one(input_dictionary, input_list=[0,3,6]):

    dict_spoken_turn_most_recent = input_dictionary.copy()
    dict_spoken_turn_previous = input_dictionary.copy()
    current_turn = 1
    max_turns = 5 # goal: 2020

    for x in range(len(input_list)): # first few turns:
        print(f'------------------turn: {current_turn}--------------------')
        print(f'player in turn {current_turn} speaks *starting* number: {input_list[x]}')
        dict_spoken_turn_most_recent[input_list[x]] = current_turn # unnecessary for starting numbers, but FIX THIS IF STARTING NUMBERS WERE, IN THEORY, REPEATED!
        current_turn += 1
        last_number_spoken = input_list[x]


    while current_turn <= max_turns:
        print(f'------------------turn: {current_turn}--------------------')
        print(f'line {line_number()}------last_number_spoken: {last_number_spoken}, __________ ')
        print(f'line {line_number()} ~~~~~~ entire dict_spoken_turn_most_recent is {dict_spoken_turn_most_recent}') # 
        print(f'line {line_number()} ~~~~~~ entire dict_spoken_turn_previous is {dict_spoken_turn_previous}') # 
        if dict_spoken_turn_previous[last_number_spoken] == 'never':
            new_number_to_speak = 0
            difference = 0
        else: 
            temp_new_most_recent = dict_spoken_turn_most_recent[new_number_to_speak]
            dict_spoken_turn_previous[new_number_to_speak] = temp_new_most_recent # add it
            dict_spoken_turn_most_recent[new_number_to_speak] = current_turn 

            difference = dict_spoken_turn_most_recent[new_number_to_speak] = dict_spoken_turn_previous[new_number_to_speak]

        new_number_to_speak = difference
        print(f'line {line_number()} difference is {difference}') # 
        print(f'line {line_number()} player in turn {current_turn} speaks new_number_to_speak: {new_number_to_speak}')
        
        current_turn += 1
        last_number_spoken = new_number_to_speak

    # NOTES:
        # https://github.com/PdxCodeGuild/class_orca/blob/main/1%20Python/docs/13%20-%20Dictionaries.md  
    # print(f'line {line_number()}-------------------------------')
    # print(f'line {line_number()} END. ~~~~~~ entire dict_spoken_turn_most_recent is {dict_spoken_turn_most_recent}')
    # print(f'line {line_number()} END. ~~~~~~ entire dict_spoken_turn_previous is {dict_spoken_turn_previous}')
    return 

example_input = {
    # 'number': 'TURN last spoken'
    0: 'never',
    3: 'never', 
    6: 'never',
}
part_one(example_input)

##############################################################################











dictionary_of_numbers = {
    16: 0, 
    11: 0, 
    15: 0, 
     0: 0,
     1: 0,
     7: 0,
}
# part_one(dictionary_of_numbers, [16,11,15,0,1,7])

##############################################################################
################## Your puzzle input is 16,11,15,0,1,7. ######################
##############################################################################
# --- Day 15: Rambunctious Recitation ---

# In this game, the players take turns saying numbers. They begin by taking turns reading from a list of starting numbers (your puzzle input). Then, each turn consists of considering the most recently spoken number:

#     If that was the first time the number has been spoken, the current player says 0.
#     Otherwise, the number had been spoken before; the current player announces how many turns apart the number is from when it was previously spoken.

# So, after the starting numbers, each turn results in that player speaking aloud either 0 (if the last number is new) or an age (if the last number is a repeat).
