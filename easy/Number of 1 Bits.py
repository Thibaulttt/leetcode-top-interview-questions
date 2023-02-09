class Solution:
  def hammingWeight(self, n: int) -> int:
    r = 0
    for c in str(n):
      if c == "1":
          r += 1
    return r
    
# n = "00000000000000000000000000001011"

solution = Solution()
print(solution.hammingWeight("00000000000000000000000000001011"))
