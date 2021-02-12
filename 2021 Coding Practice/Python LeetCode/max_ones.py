# https://leetcode.com/explore/featured/card/fun-with-arrays/521/introduction/3238/
# Example 1:
# Explanation: The first two digits or the last three digits are consecutive 1s.
#     The maximum number of consecutive 1s is 3.
# Note:
#     The input array will only contain 0 and 1.
#     The length of input array is a positive integer and will not exceed 10,000

def findMaxConsecutiveOnes(nums: list[int]) -> int: #remember took away self (not using class model, and List > list for lowercase python!)
    print(f'start')
    counter = 0
    final_list = []

    for num in nums:
        # temp_i = i
        # print(f'i is now: {i}')
        # try:
        #     if nums[i] == 1:
        #         consecutive_ones = 1
        #         # max_consecutive_ones = consecutive_ones
        #         while nums[i+1] == 1:
        #             consecutive_ones += 1
        #             print(f'nums[{i}] : {nums[i]}, consecutive_ones now: {consecutive_ones}')
        #             i += 1
        #         else:
        #             if consecutive_ones > max_consecutive_ones:
        #                 max_consecutive_ones = consecutive_ones
        #             print(f'ELSE STATEMENT HERE WITH nums[{i}] : {nums[i]}, consecutive_ones now: {consecutive_ones}. .... max_consecutive_ones: {max_consecutive_ones}')
        #     i = temp_i # reset i:
        # except IndexError:
        #     print('index error')
        # i += 1
        if num == 1:
            counter += 1
            final_list.append(counter)
        else:
            final_list.append(counter)
            counter = 0
        if final_list == []: # edge case of single list: [1]
            final_list.append(counter)
    # print(f'returning max_consecutive_ones: {max_consecutive_ones}')
    # return max_consecutive_ones
    print(final_list)
    final_list.sort()
    print(final_list[-1])
    return final_list[-1]

# LOOKUP HASH TABLE!
# Hash Table...
test_list_1 = [1,1,0,1,1,1,0,0,5,1,1,1,1,0,9,6] # len = 16
test_list_2 = [1]
test_list_3 = [0,1]
print(findMaxConsecutiveOnes(test_list_1))
# findMaxConsecutiveOnes(test_list_2)
# findMaxConsecutiveOnes(test_list_3)

print('~~~~~~~~FINISH~~~~~~~')