class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n//3 > 0:
          if n%3 > 0:
              return False
          if n == 3:
             return True
          n = n//3
        return False

solution = Solution()
print(solution.isPowerOfThree(1))
print(solution.isPowerOfThree(2))
print(solution.isPowerOfThree(3))
print(solution.isPowerOfThree(9))
print(solution.isPowerOfThree(27))
print(solution.isPowerOfThree(81))
print(solution.isPowerOfThree(28))
