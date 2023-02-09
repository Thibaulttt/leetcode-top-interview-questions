from itertools import product
from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if d == "":
            return []
        p = []
        for d in digits:
            if d == '2':
                p.append('abc')
            elif d == '3':
                p.append('def')
            elif d == '4':
                p.append('ghi')
            elif d == '5':
                p.append('jkl')
            elif d == '6':
                p.append('mno')
            elif d == '7':
                p.append('pqrs')
            elif d == '8':
                p.append('tuv')
            elif d == '9':
                p.append('wxyz')
        return ["".join(c) for c in product(*p)]

solution = Solution()
print(solution.letterCombinations("23"))
print(list(product('abc', 'def')))