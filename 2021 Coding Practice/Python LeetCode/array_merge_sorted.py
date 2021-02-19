# # https://leetcode.com/explore/learn/card/fun-with-arrays/525/inserting-items-into-an-array/3253/

# def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
def merge(nums1, m, nums2, n): # nums1/2 are the arrays, m and n are the numbers initialized
    """
    Do not return anything, modify nums1 in-place instead.
    """
    c1 = 0 # counter 1
    c2 = 0
    while c1 < m:
        print(f'c1 is {c1}')
        c1 += 1

    nums1.sort()
    print(nums1)
    return
        
nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 6]
merge(nums1, 3, nums2, 3)

# merge first
# then

# nums1 = [1]
# nums2 = []
# merge(nums1, 1, nums2, 0)


# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
# The number of elements initialized in nums1 and nums2 are m and n respectively. You may assume that nums1 has a size equal to m + n such that it has enough space to hold additional elements from nums2.

# Example 1:

    # Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
    # Output: [1,2,2,3,5,6]

# Example 2:

    # Input: nums1 = [1], m = 1, nums2 = [], n = 0
    # Output: [1]

# Constraints:
#     nums1.length == m + n
#     nums2.length == n
#     0 <= m, n <= 200
#     1 <= m + n <= 200
#     -109 <= nums1[i], nums2[i] <= 109

