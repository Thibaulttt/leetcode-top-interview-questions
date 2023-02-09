from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        for n in nums:
            if n not in d:
                d[n] = 1
            else:
                d[n] = d.get(n)+1
        return max(d.items(), key=lambda x: x[1])[0]

nums = [3,2,3,1,1,1,1,1]
# nums = [2,2,1,1,1,2,2]

solution = Solution()
print(solution.majorityElement(nums))
