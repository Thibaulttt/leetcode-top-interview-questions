from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        reds = nums.count(0)
        whites = nums.count(1)
        blues = len(nums)-(reds+whites)

        for i in range(reds):
            nums[i] = 0
        for i in range(whites):
            nums[i+reds] = 1
        for i in range(blues):
            nums[i+whites+reds] = 2
        
        print(nums)

solution = Solution()
solution.sortColors([2,0,2,1,1,0])
solution.sortColors([2,0,1])