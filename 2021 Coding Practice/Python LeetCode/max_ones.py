# https://leetcode.com/explore/featured/card/fun-with-arrays/521/introduction/3238/
# Example 1:
# Explanation: The first two digits or the last three digits are consecutive 1s.
#     The maximum number of consecutive 1s is 3.
# Note:
#     The input array will only contain 0 and 1.
#     The length of input array is a positive integer and will not exceed 10,000

def findMaxConsecutiveOnes(nums: list[int]) -> int: #remember took away self (not using class model, and List > list for lowercase python!)
    i = 0

    print(f'start,')

    for number in nums:
        temp_i = i
        try:
            if nums[i] == 1:
                max_consecutive_ones = 1
                while nums[i+1] == 1:
                    max_consecutive_ones += 1
                    print(f'nums[{i}] : {nums[i]}, max_consecutive_ones now: {max_consecutive_ones}')
                    i += 1
            i = temp_i # reset i:

        except IndexError:
            print('index error')

        i += 1
        print(f'i is now: {i}')

    return max_consecutive_ones

test_list_1 = [1,1,0,1,1,1,8,67,5,1,1,1,1,0,9,6]
print(len(test_list_1))
findMaxConsecutiveOnes(test_list_1)

print('~~~~~~~~~~~~~~~')