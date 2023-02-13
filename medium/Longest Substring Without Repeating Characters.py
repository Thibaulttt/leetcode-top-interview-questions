class Solution:
    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     if len(s) == 0:
    #         return 0
    #     if len(s) == 1:
    #         return 1
    #     longest = 1
    #     temp = ""
    #     for c in s:
    #         if c in temp:
    #             if len(temp) > longest:
    #                 longest = len(temp)
    #             temp = ""
    #         temp += c
    #     return len(temp) if len(temp) > longest else longest
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_l = 0
        stack = ""

        for i, c in enumerate(s):
            if c not in stack:
                stack += c
            else:
                stack = stack[stack.index(c)+1:]
                stack += c
            max_l = max(max_l, len(stack))
        
        return max_l

solution = Solution()
print(solution.lengthOfLongestSubstring("abcabcbb"))
print(solution.lengthOfLongestSubstring("bbbbb"))
print(solution.lengthOfLongestSubstring("pwwkew"))
print(solution.lengthOfLongestSubstring("pwwablwwkew"))
print(solution.lengthOfLongestSubstring("a"))
print(solution.lengthOfLongestSubstring(" "))
print(solution.lengthOfLongestSubstring(""))
print(solution.lengthOfLongestSubstring("au"))
print(solution.lengthOfLongestSubstring("dvdf"))
print(solution.lengthOfLongestSubstring("devdf"))