class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        print(list(reversed(columnTitle)))
        for i, c in enumerate(list(reversed(columnTitle))):
            if i == 0:
              res += ord(c)-64
            else:
              res += (ord(c)-64)*(26**i)
        return res

solution = Solution()
# print(solution.titleToNumber("A"))
# print(solution.titleToNumber("AA"))

# A = 1
print(solution.titleToNumber("A"))
# Z = 26
print(solution.titleToNumber("Z"))
# AA = 27 = 26*1 + 1
print(solution.titleToNumber("AA"))
# AB = 28 = 26*1 + 2
print(solution.titleToNumber("AB"))
# AZ = 52 = 26*1 + 26
print(solution.titleToNumber("AZ"))
# BA = 53 = 26*2 + 1
print(solution.titleToNumber("BA"))
# BB = 54 = 26*2 + 2
print(solution.titleToNumber("BB"))
# BZ = 78 = 26*2 + 26
print(solution.titleToNumber("BZ"))
# CA = 79 = 26*3 + 1
print(solution.titleToNumber("CA"))
# ZZ = 702 = 26*26 + 26
print(solution.titleToNumber("ZZ"))
# AAA = 703 = 26*26*1 + 26*1 + 1
print(solution.titleToNumber("AAA"))
# AAB = 704 = 26*26*1 + 26*1 + 2
print(solution.titleToNumber("AAB"))
# ABA = 704 = 26*26*1 + 26*2 + 1
print(solution.titleToNumber("ABA"))
