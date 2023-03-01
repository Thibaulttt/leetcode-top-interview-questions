from typing import List

class Solution:
    # def findDuplicate(self, nums: List[int]) -> int:
    #     for i, n in enumerate(nums):
    #         if i < len(nums)-1 and n in nums[i+1:]:
    #             return n
    
    def findDuplicate(self, nums: List[int]) -> int:
        nums_set = set()
        for n in nums:
            if n in nums_set:
                return n
            nums_set.add(n)

solution = Solution()
print(solution.findDuplicate([1,3,4,2,2]))
