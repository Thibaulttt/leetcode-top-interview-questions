from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max = 0
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                if i != j:
                    l = j-i
                    h = min(height[i], height[j])
                    area = l*h
                    if area > max:
                        max = area
        return max
    
solution = Solution()
print(solution.maxArea([1,8,6,2,5,4,8,3,7]))
print(solution.maxArea([1,2,1]))
