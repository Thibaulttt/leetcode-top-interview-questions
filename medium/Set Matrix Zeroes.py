from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeroes = (set(), set())

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    zeroes[0].add(i)
                    zeroes[1].add(j)
                else:
                    if i in zeroes[0] or j in zeroes[1]:
                        matrix[i][j] = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] != 0:
                    if i in zeroes[0] or j in zeroes[1]:
                        matrix[i][j] = 0
        
        print(matrix)
                
                    
       


solution = Solution()
solution.setZeroes([[1,1,1],[1,0,1],[1,1,1]])
solution.setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]])