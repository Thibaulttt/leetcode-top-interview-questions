from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i, n in enumerate(nums2):
            nums1[m+i] = n
        nums1.sort()
        print(nums1)

solution = Solution()
solution.merge([1,2,3,0,0,0], 3, [2,5,6], 3)
solution.merge([1], 1, [], 0)
solution.merge([0], 0, [1], 1)
solution.merge([4,5,6,0,0,0], 3, [1,2,3], 3)
solution.merge([4,0,0,0,0,0], 1, [1,2,3,5,6], 5)