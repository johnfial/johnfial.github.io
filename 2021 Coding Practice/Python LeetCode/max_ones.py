# https://leetcode.com/explore/featured/card/fun-with-arrays/521/introduction/3238/
# Example 1:

# Input: [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s.
#     The maximum number of consecutive 1s is 3.

# Note:

#     The input array will only contain 0 and 1.
#     The length of input array is a positive integer and will not exceed 10,000


test_list_1 = [1,1,0,1,1,1]

def findMaxConsecutiveOnes(nums: list[int]) -> int: #remember took away self (not using class model, and List > list for lowercase python!)
    i = 0
    max_ones = 0

    print(f'start, max_ones now: {max_ones}')

    for number in nums:
        try:
            if nums[i] == 1:
                if nums[i+1] == 1:
                    max_ones += 1
                    print(f'nums[{i}] : {nums[i]}, max_ones now: {max_ones}')
                i += 1
                print(f'i: {i}')        
        
    return max_ones

findMaxConsecutiveOnes(test_list_1)

print('~~~~~~~~~~~~~~~')