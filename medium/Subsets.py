from typing import List

class Solution:
    # def subset(self, nums):
    #     yield nums
    #     if len(nums) == 1:
    #         pass
    #     else:
    #         for i in range(len(nums)):
    #             yield from self.subset(nums[:i] + nums[i+1:])
    
    def subset(self, nums, res):
        if nums not in res:
            res.append(nums)
            if len(nums) > 1:
              for i in range(len(nums)):
                  self.subset(nums[:i] + nums[i+1:], res)

    # def subsets(self, nums: List[int]) -> List[List[int]]:
    #     res = []
    #     print(list(self.subset(nums)))
    #     for l in self.subset(nums):
    #         if l not in res:
    #             res.append(l)
    #     res.append([])
    #     return res

    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.subset(nums, res)
        res.append([])
        return res

solution = Solution()
print(solution.subsets([1,2,3]))
print(solution.subsets([0]))
# print(solution.subsets([1,2,3,4,5,6,7,8,10,0]))