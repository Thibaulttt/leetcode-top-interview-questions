from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occur = dict()
        for n in nums:
            if n not in occur.keys():
                occur[n] = 1
            else:
                occur[n] += 1
        
        return list(dict(sorted(occur.items(), key=lambda x: x[1], reverse=True)).keys())[:k]
    
    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     occur = dict()
    #     for n in nums:
    #         if n not in occur.keys():
    #             occur[n] = 1
    #         else:
    #             occur[n] += 1
    #     most_freq = []
    #     while len(most_freq) < k:
    #         m = max(occur, key=occur.get)
    #         most_freq.append(m)
    #         del occur[m]
    #     return most_freq

solution = Solution()
print(solution.topKFrequent([1,1,1,2,2,3], 2))
print(solution.topKFrequent([1,1,1,2,2,3], 1))
