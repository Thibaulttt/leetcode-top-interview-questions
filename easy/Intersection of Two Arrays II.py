from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        if len(nums1) > len(nums2):
          for n in nums2:
              if n in nums1:
                  res.append(n)
                  nums1.remove(n)
        else:
            for n in nums1:
              if n in nums2:
                  res.append(n)
                  nums2.remove(n)  
        
        return res

nums1 = [1,2,2,1]
nums2 = [2,2]

solution = Solution()
print(solution.intersect(nums1, nums2))