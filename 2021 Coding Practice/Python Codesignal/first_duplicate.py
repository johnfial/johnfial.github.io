# https://app.codesignal.com/interview-practice/task/pMvymcahZ8dY4g75q/description
# Example

#     For a = [2, 1, 3, 5, 3, 2], the output should be firstDuplicate(a) = 3.

#     There are 2 duplicates: numbers 2 and 3. The second occurrence of 3 has a smaller index than the second occurrence of 2 does, so the answer is 3.

#     For a = [2, 2], the output should be firstDuplicate(a) = 2;

#     For a = [2, 4, 3, 5, 1], the output should be firstDuplicate(a) = -1.


def firstDuplicate(list):

    result = -1
    index = 0

    while index <= len(list)-1: # check on the -1 !
        
        index += 1

    return result
# firstDuplicate(a1)
# firstDuplicate(a2)
# firstDuplicate(a3)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

a1 = [2, 1, 3, 5, 3, 2]
a2 = [2, 2]
a3 = [2, 4, 3, 5, 1]

def containsDuplicates(input_list):
    result = False

    index = 0

    while index+1 < len(input_list):
        number_popped = input_list.pop(index)
        print(f'index = {index}, popped: {number_popped}, list: {input_list}')
        
        if number_popped in input_list:
            # print('DUPLICATE!!!')
            result = True
            input_list.insert(index, number_popped) # put it back
            index += 1
        else:
            input_list.insert(index, number_popped) # put it back
            index += 1
    # print(f'result: {result}')
    return result

containsDuplicates(a1)
# containsDuplicates(a2)
# containsDuplicates(a3)