from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # for row, i in enumerate(matrix):
        #     row[len(row) - i] = row[i]

        res = [[None for i in range(len(matrix))] for _ in range(len(matrix))]

        for i in range(len(matrix)):
            for j in range(len(matrix)):
                res[j][i] = matrix[i][j]
            
        for i in range(len(matrix)):
            matrix[i] = list(reversed(res[i]))
        
        print(matrix)
        

solution = Solution()

matrix = [[1,2,3],[4,5,6],[7,8,9]]
solution.rotate(matrix)

matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
