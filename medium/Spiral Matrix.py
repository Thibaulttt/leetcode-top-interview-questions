from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        while matrix != []:
          res += matrix[0]
          matrix.pop(0)

          for row in matrix[:-1]:
              if len(row) > 0:
                res.append(row[-1])
                row.pop(-1)

          if len(matrix) > 0:
            res += reversed(matrix[-1])
            matrix.pop(-1)

          for row in reversed(matrix):
              if len(row) > 0:
                res.append(row[0])
                row.pop(0)

        return res, matrix

solution = Solution()
# print(solution.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
# print(solution.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
# print(solution.spiralOrder([[5]]))
# print(solution.spiralOrder([[6, 7]]))
# print(solution.spiralOrder([[7],[9],[6]]))
# print(solution.spiralOrder([[1,2],[3,4]]))
# print(solution.spiralOrder([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]]))
print(solution.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]))