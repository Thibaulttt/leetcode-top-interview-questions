from typing import List

# [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1

# class Solution:
#   def generate(self, numRows: int) -> List[List[int]]:
#     res = [[1]]

#     for i in range(1, numRows):
#       row = []
#       for j in range(0,i+1):
#         print(i-1, j-1, i, j)
#         row.append(res[i-1][j-1])
#         if j != i:
#           print(res[i-1][j])
#           row.append(res[i-1][j-1] + res[i-1][j])
#       res.append(row)
#       print(res)

#     return res

# solution = Solution()

# numRows = 4

# print(solution.generate(numRows))

class Solution:
  def generate(self, numRows: int) -> List[List[int]]:
    res = []

    res.append([1])
    res.append([1, 1])

    for i in range(2, numRows):
      row = []

      row.append(1)
      for j in range(1, i-1):
        print(i, j, int((i+1)/2), res)
        if j < int((i+1)/2):
          row.append(res[i-1][j-1] + res[i-1][j])
        if j > int((i+1)/2):
          row.append(res[i-1][j-2] + res[i+1][j-1])
        # elif j != i:
        #   row.append(res[i-1][j-1] + res[i-1][j-1])
        # else:
        #   row.append(res[i-1][j-1])
      row.append(1)
      res.append(row)

    return res

solution = Solution()

numRows = 8

print(solution.generate(numRows))

