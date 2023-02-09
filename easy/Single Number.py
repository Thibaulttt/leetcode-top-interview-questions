from typing import List

# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

class Solution:
  def singleNumber(self, nums: List[int]) -> int:
    once = set()
    for n in nums:
      if n in once:
        once.remove(n)
      else:
        once.add(n)
    return 0 if len(once) == 0 else once.pop()

nums = [4,1,2,1,2]
nums = [1,2,1,2]
nums = [1]

solution = Solution()
print(solution.singleNumber(nums))