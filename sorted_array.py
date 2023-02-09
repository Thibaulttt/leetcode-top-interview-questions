m = 3
n = 3
nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
# nums1 = list(sorted(nums1[:m] + nums2[:n]))

print(nums1, nums2)

# nums1.length == m + n
# nums2.length == n

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if len(nums1) == 0 or len(nums2) == 0:
          return
        j = 0
        for i in range(n):
          print(nums1[j], nums2[i])
          if nums1[j] < nums2[i]:
            nums1[n+j] = nums2[i]
            nums1[j+1] = nums1[j]
            j += 1
          elif nums1[j] > nums2[i]:
            nums1[m+j] = nums2[i]

          print(nums1, nums2)


Solution.merge(None, nums1, m, nums2, n)
