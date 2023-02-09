from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # if min(nums) > 0:
        #    return 0
        # prev = None
        # for n in sorted(nums):
        #     if prev and n != prev+1:
        #       return prev+1
        #     else:
        #       prev = n
        # return prev+1
        prev = 0
        for n in sorted(nums):
            if prev != n:
                return prev
            prev = n+1
        return prev
    
# [3,0,1]
# [0,1]
# [9,6,4,2,3,5,7,0,1]

solution = Solution()
print(solution.missingNumber([3,0,1]))
print(solution.missingNumber([0,1]))
print(solution.missingNumber([9,6,4,2,3,5,7,0,1]))
print(solution.missingNumber([1,2]))
