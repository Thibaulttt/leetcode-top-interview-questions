from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1, -1]
        return [nums.index(target), len(nums)-1-list(reversed(nums)).index(target)]

solution = Solution()
print(solution.searchRange([5,7,7,8,8,10], 8))
print(solution.searchRange([5,7,7,8,8,10], 6))
print(solution.searchRange([], 0))