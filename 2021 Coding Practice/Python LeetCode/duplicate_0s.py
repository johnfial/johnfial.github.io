# class Solution:
#     def duplicateZeros(self, arr: List[int]) -> None:
#         """
#         Do not return anything, modify arr in-place instead.
#         """
        

def duplicateZeroes(arr):
    temp_array = []
    for num in arr:
        if num == 0:
            temp_array.append(0)
            temp_array.append(0)
        else:
            temp_array.append(num)
    print(arr)
    arr = temp_array
    print(arr)
    return

example_1 = [1,0,2,3,0,4,5,0]   # Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
example_2 = [0,1,2,3] # Explanation: After calling your function, the input array is modified to: [1,2,3]
print(duplicateZeroes(example_1))
