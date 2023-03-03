from typing import List

# [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1

class Solution:
  def generate(self, numRows: int) -> List[List[int]]:
    if numRows == 1:
      return [1]
    
    elif numRows == 2:
      return [1,1]
    
    res = [[1], [1, 1]]

    for i in range(2,numRows):
      res.append([])
      for j in range(len(res[i-1])+1):
        if j == 0 or j == len(res[i-1]):
          res[i].append(1)
        else:
          previous_sum = res[i-1][j-1] + res[i-1][j]
          res[i].append(previous_sum)

    return res

solution = Solution()

numRows = 8

print(solution.generate(numRows))

