from typing import List
# nums = [3,2,1,0,4]

# next_jump = nums[0]

# for i, n in enumerate(nums):
#   print(i, n, next_jump)
#   if i == next_jump:
#     next_jump = n
#   print(i, n, next_jump)
#   if next_jump == 0:
#     exit()

# print(i, len(nums)-1)

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        next_jump = nums[0]
        
        for i, n in enumerate(nums):
            # print(i, n, next_jump)
            if n == 0 and i != len(nums):
                return False
            if next_jump + 1 == len(nums):
                return True
            if i  == next_jump:
                next_jump = n + i
            # print(i, n, next_jump)
            # print()
        return i == next_jump

nums = [2,3,1,1,4]
nums = [2,0,0]
nums = [2,5,0,0]
nums = [2,3,1,1,4,6,8,9,10,11]
solution = Solution()
print(solution.canJump(nums))