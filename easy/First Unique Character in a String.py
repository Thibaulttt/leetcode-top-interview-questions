class Solution:
    # def firstUniqChar(self, s: str) -> int:
    #     uniq = False
    #     for i in range(len(s)-1):
    #         for c in s[i+1:]:
    #             uniq = True
    #             if s[i] == c:
    #                 uniq = False
    #                 break
    #         print(uniq, s[i])
    #         if uniq:
    #           return i
    #     return -1
    
    def firstUniqChar(self, s: str) -> int:
        for i in range(len(s)):
            uniq = True
            for j in range(len(s)):
                if i!=j and s[i] == s[j]:
                    uniq = False
                    break
            if uniq:
                return i
        return -1

solution = Solution()
s = "leetcode"
# s = "loveleetcode"
# s = "aabb"
print(solution.firstUniqChar(s))
