from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        for i, n in enumerate(nums[:]):
            if n == 0:
                nums.remove(n)
                nums.append(0)
        return nums

# [0,1,0,3,12]
# [0,1,3,12]
# [0]

solution = Solution()
print(solution.moveZeroes([0,1,0,3,12]))
print(solution.moveZeroes([0,0,1]))
