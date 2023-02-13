class Solution:
  # def hammingWeight(self, n: int) -> int:
  #   r = 0
  #   for c in str(n):
  #     if c == "1":
  #         r += 1
  #   return r
  def hammingWeight(self, n: int) -> int:
    return str(bin(n)).count("1")

solution = Solution()
n = int("00000000000000000000000000001011", base=2)
print(solution.hammingWeight(n))
