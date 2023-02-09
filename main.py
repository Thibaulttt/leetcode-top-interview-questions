# class Solution:
#   def removeDuplicates(self, nums: list[int]) -> int:
#     if len(nums) < 1:
#       return len(nums), nums
#     prev = nums[0]
#     for i, cur in enumerate(nums):
#       print(nums, prev, cur, i)
#       if cur == prev:
#         nums.pop(i)
#         print(nums)
#       prev = cur
#     return len(nums), nums

# print(Solution.removeDuplicates(None, [0,0,1,1,1,2,2,3,3,4]))

# class Solution:
#   def removeDuplicates(self, nums: list[int]) -> int:
#     if len(nums) < 1:
#       return len(nums), nums
#     uniq = set(nums)
#     nums[:] = list(uniq)
#     return len(uniq), list(uniq)

# print(Solution.removeDuplicates(None, [1,1,2]))

class Solution:
  def removeDuplicates(self, nums: list[int]) -> int:
    if len(nums) < 1:
      return len(nums), nums
      
    # for i in range(1, len(nums)):
    #   print(nums, "prev",  nums[i-1], "cur", nums[i], "i", i)
    #   if nums[i-1] == nums[i]:
    #     nums.pop(i)
    
    i = 1
    while i < len(nums):
      if nums[i-1] == nums[i]:
        nums.pop(i)
        i -= 1
      i += 1
    return len(nums), nums

print(Solution.removeDuplicates(None, [0,0,1,1,1,1,2,2,3,3,4]))