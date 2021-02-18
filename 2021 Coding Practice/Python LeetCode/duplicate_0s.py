# class Solution:
#     def duplicateZeros(self, arr: List[int]) -> None:
#         """
#         Do not return anything, modify arr in-place instead.
#         """
        

def duplicateZeroes(arr):
    # temp_array = []
    # for num in arr:
    #     if len(temp_array) < len(arr):
    #         if num == 0:
    #             temp_array.append(0)
    #             temp_array.append(0)
    #         else:
    #             temp_array.append(num)
    # print(arr)
    # arr = temp_array
    # print(arr)

    i = 0
    length = len(arr)
    for num in range(0, len(arr)):
        while len(arr) <= length:
            if arr[num] == 0:
                arr.insert(i, 0)
                # i += 1
            # else:
            #     i += 1
    print(arr)

arr = [1,0,2,3,0,4,5,0]   # Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
example_2 = [1,2,3] # Explanation: After calling your function, the input array is modified to: [1,2,3]
# duplicateZeroes(example_2)
duplicateZeroes(arr)
