# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/727/

def removeDuplicates(numlist):
    templist = []
    for number in numlist:
        if number not in templist:
            templist.append(number)
            # print(f'len(templist): {len(templist)} and templist: {templist} ')
    numlist = templist
    return numlist
        


list2 = [0, 0, 0, 1, 1, 3, 9, 4, 7, 7]

print('#####################')
print(removeDuplicates(list2))
print('#####################')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# Example 2:

# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4]