from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for s in strs:
            s_sorted = ''.join(sorted(s))
            if s_sorted not in anagrams:
                anagrams[s_sorted] = [s]
            else:
                anagrams[s_sorted].append(s)
        
        return list(anagrams.values())

solution = Solution()
print(solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(solution.groupAnagrams(["cab","tin","pew","duh","may","ill","buy","bar","max","doc"]))

