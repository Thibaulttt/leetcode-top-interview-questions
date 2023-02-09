class Solution:
    def isHappy(self, n: int) -> bool:
        seq = set()
        while n != 1:
            n = sum([int(c)**2 for c in str(n)])
            if n not in seq:
              seq.add(n)
            else:
              return False
        return True

solution = Solution()
print(solution.isHappy(2))
print(solution.isHappy(19))
