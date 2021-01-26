##############################################################################
# John Fial, PDX Code Guild, 2020-2021, www,johnfial.com
##############################################################################

# https://adventofcode.com/2020/day/4
# description pasted @ bottom
# cd C:\-=Cloud=-\Sync\git_working\weeks8-12_advent_christmas_december_calendar

import inspect
def line_number():
    """Returns the current line number in our program."""
    return inspect.currentframe().f_back.f_lineno

# ##############################################################################
# # --- Day 6: Custom Customs ---
# # --- Part One START ---
# file_to_open = 'day06.txt'
# with open(file_to_open, 'r') as file:
#     # customs_data = file.read()
#     customs_example = file.read()
# # customs_example = '''abcx
# # abcy
# # abcz

# # abc

# # a
# # b
# # c

# # ab
# # ac

# # a
# # a
# # a
# # a

# # b'''
# customs_example = customs_example.split("\n\n") # lines() # split("\n\n")
# # print(f'raw list is: {customs_example}, len(customs_example) {len(customs_example)}: ')

# i=0
# for answer in customs_example:
#     # print(customs_example[i])
#     customs_example[i] = customs_example[i].replace("\n", "") # string.replace("\n", "")    
#     # print(customs_example[i])
#     i += 1
# print(f'raw list is NOW, no \\n : {customs_example}, len(customs_example) {len(customs_example)}: ')

# sum_total = 0
# for answers in customs_example:
#     empty_list = []

#     # print(answers)
#     for i in range(len(answers)):
        
#         letter = answers[i]
        
#         if answers[i] not in empty_list:
#             empty_list.append(letter)
#         else:
#             pass # print(f'passed letter {letter}')

#     print(f'len(empty_list) is: {len(empty_list)} for answers: {answers}')
#     sum_total += len(empty_list)

# print(f'sum_total is: {sum_total} for len(customs_example) {len(customs_example)}')

# # --- Day 6: Custom Customs ---
# # --- Part One END---
# ##############################################################################




##############################################################################
# --- Day 6: Custom Customs ---
# --- Part Two ---
file_to_open = 'day6_1.txt'
with open(file_to_open, 'r') as file:
    customs_data = file.read()
    # customs_example = file.read()
customs_example = '''abcx
abcy
abcz

abc

a
b
c

ab
ac

a
a
a
a

b'''
customs_example = customs_example.split("\n\n") 

    # # WORKS FOR TWO LISTS:
    # list1 = [1, 2, 3, 4, 5]
    # list2 = [2, 3, 4, 5, 6]
    # def find_intersections(A, B):
    #     intersections_list = []
    #     for number in A:
    #         if number in B:
    #             intersections_list.append(number)
    # find_intersections(list1, list2)
    # print(f'intersections_list is now {intersections_list}') 



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

intersection_list = [] # this pairs with below function:
def find_intersections(container_list, index=0):

    index += 1
    # intersection_list = set(container_list[index-1]).intersection(container_list[index])
    # print(f' intersection_list : {intersection_list} ')

    # # can you overwrite a set?
    # intersection_list = set(container_list[index+1]).intersection(container_list[index+2])
    # print(f' intersection_list : {intersection_list} ')

    
    # # print(''.join(set(word_1).intersection(word_2)))
    # # print(len(''.join(set(word_1).intersection(word_2))))

    # while True:

    #     # THIS IS THE INNER END FUNCTION:
    #     if index == len(container_list):
    #         print('this is the inner russian doll!~~~~~~~~~~~~~~~~')
    #         print(f'inside the matrix, break While Loop !')
    #         print(f'container_list[{index}] is {container_list[index]} and intersection_list : {intersection_list}') 
    #         break

    #     for number in container_list[index-1]:
    #         if number in container_list[index]:
    #             intersection_list.append(number)
    #     print(f'end while loop with intersection_list : {intersection_list} ') 
    #     index += 1
    # print(f'intersection_list is now {intersection_list}, running return and recursive function...') 
    # return find_intersections(intersection_list, index)        
    print(f'running return intersection_list : {intersection_list} ') # type 'set'
    # print(f'running return intersection_list : {intersection_list[3]} ') 
    return intersection_list

num_lists = [
        [1, 2, 3, 4, 5],
        [2, 3, 4, 5, 6],
        [3, 4, 5, 6, 7],
        [4, 5, 6, 7, 8],
] # len = 4

# find_intersections(num_lists)
# print(find_intersections(num_lists))

# def get_intersection(outer_list, index=0):
#     # Check out the sum example below and try to do the same thing with set intersections!
#     numbers_in_common 
#     inner_list = outer_list[index]
#     print(f'current inner_list: {inner_list} and index {index}, ')
#     index += 1

#     if index == len(outer_list):
#         return inner_list

#     return something + get_intersection(something, index)

# print(get_intersection(num_lists))

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    # sum of list with recursion:
nums = [1, 2, 3, 4, 5, 10]
def get_sum(list_of_nums, index=0):
    num = list_of_nums[index]
    index += 1
  
    if index == len(list_of_nums):
        return num
    # print(f'current num: {num} and index {index}, ')
    return num + get_sum(list_of_nums, index)

print(get_sum(nums))

# # # # # # # # # # # # # # # # 




sum_total = 0

for group in customs_example: 
    
##############################################################################
##############################################################################
    ############### LEAVING OFF HERE, 5 DEC PM, 
    # Have each group as a list of strings WITHIN the customs_data list itself
    # Now I need to check if a letter is SHARED between EVERY member of the list ############### 
    
    # print(f'len(group) {len(group)}')
    group_total = 0
    individual_answers = group.splitlines()
    # print(f'type(individual_answers) : {type(individual_answers)}, len(individual_answers): {len(individual_answers)}')
    
    # print(set(individual_answers[0]).intersection(individual_answers[1]).intersection(individual_answers[2]))
    i = 0
    for answer in individual_answers:
                # MESSAGE TO PETE: 
                        # Basically I need a line of code that's variable, 
                # which I assume might be a common thing in writing code...
                # I want the intersection of ALL strings in a list. That line is: 

                # set(listA[1]).intersection(listA[2])).listA(individual_answers[3])

                # but it's much harder for five intersections, and I have no idea if it's 
                # possible to write such a complicated line for a variable # of intersections, 
                # depending on the number of strings in the list...
        # print(answer)
        pass
        # i += 1
        
    # https://stackoverflow.com/questions/48611525/find-common-characters-between-two-strings
    # https://docs.python.org/3/library/stdtypes.html#frozenset.intersection
            # word_1 = 'one'
            # word_2 = 'toe'

            #    v join the intersection of `set`s to get back the string
            #    v                             v  No need to type-cast it to `set`.
            #    v                             v  Python takes care of it
            # print(''.join(set(word_1).intersection(word_2)))
            # print(len(''.join(set(word_1).intersection(word_2))))




print(f'sum_total is: *** {sum_total} *** --------------- ( for len(customs_example) {len(customs_example)} )')
##############################################################################
##############################################################################
##############################################################################













##############################################################################
# --- Part Two ---

# As you finish the last group's customs declaration, you notice that you misread one word in the instructions:

# You don't need to identify the questions to which anyone answered "yes"; you need to identify the questions to which everyone answered "yes"!

# Using the same example as above:

# abc

# a
# b
# c

# ab
# ac

# a
# a
# a
# a

# b

# This list represents answers from five groups:

#     In the first group, everyone (all 1 person) answered "yes" to 3 questions: a, b, and c.
#     In the second group, there is no question to which everyone answered "yes".
#     In the third group, everyone answered yes to only 1 question, a. Since some people did not answer "yes" to b or c, they don't count.
#     In the fourth group, everyone answered yes to only 1 question, a.
#     In the fifth group, everyone (all 1 person) answered "yes" to 1 question, b.

# In this example, the sum of these counts is 3 + 0 + 1 + 1 + 1 = 6.

# For each group, count the number of questions to which everyone answered "yes". What is the sum of those counts?

##############################################################################
# --- Day 6: Custom Customs ---

# As your flight approaches the regional airport where you'll switch to a much larger plane, customs declaration forms are distributed to the passengers.

# The form asks a series of 26 yes-or-no questions marked a through z. All you need to do is identify the questions for which anyone in your group answers "yes". Since your group is just you, this doesn't take very long.

# However, the person sitting next to you seems to be experiencing a language barrier and asks if you can help. For each of the people in their group, you write down the questions for which they answer "yes", one per line. For example:

# abcx
# abcy
# abcz

# In this group, there are 6 questions to which anyone answered "yes": a, b, c, x, y, and z. (Duplicate answers to the same question don't count extra; each question counts at most once.)

# Another group asks for your help, then another, and eventually you've collected answers from every group on the plane (your puzzle input). Each group's answers are separated by a blank line, and within each group, each person's answers are on a single line. For example:

# abc

# a
# b
# c

# ab
# ac

# a
# a
# a
# a

# b

# This list represents answers from five groups:

#     The first group contains one person who answered "yes" to 3 questions: a, b, and c.
#     The second group contains three people; combined, they answered "yes" to 3 questions: a, b, and c.
#     The third group contains two people; combined, they answered "yes" to 3 questions: a, b, and c.
#     The fourth group contains four people; combined, they answered "yes" to only 1 question, a.
#     The last group contains one person who answered "yes" to only 1 question, b.

# In this example, the sum of these counts is 3 + 3 + 3 + 1 + 1 = 11.

# For each group, count the number of questions to which anyone answered "yes". What is the sum of those counts?
