class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

s = "anagram"
t = "nagaram"

print(sorted(s), sorted(t))

# s = "rat"
# t = "car"

solution = Solution()
print(solution.isAnagram(s, t))