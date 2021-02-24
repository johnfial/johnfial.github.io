
def duplicateZeroes(arr):

    temp_array = []
    for num in arr:
        if len(temp_array) < len(arr):
            if num == 0:
                temp_array.append(0)
                temp_array.append(0)
            else:
                temp_array.append(num)
    arr = []
    arr = temp_array
    print(arr)
    return temp_array

# Here's a simple while loop with counter:
# https://leetcode.com/explore/learn/card/fun-with-arrays/525/inserting-items-into-an-array/3245/discuss/1077394/Python3-solution
    # i=0
    # while (i < len(arr)):
    #     if arr[i] == 0:
    #         arr.pop(-1)
    #         arr.insert(i+1,0) 
    #         i+=1 
    #     i+=1

# 3245  https://leetcode.com/explore/learn/card/fun-with-arrays/525/inserting-items-into-an-array/3245/

example_1 = [1,0,2,3,0,4,5,0]   # Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
example_2 = [1,2,3] # Explanation: After calling your function, the input array is modified to: [1,2,3]
print(example_1)
# duplicateZeroes(example_2)
duplicateZeroes(example_1)
