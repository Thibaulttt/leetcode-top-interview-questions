from typing import List

# BFS
'''
class Solution:
    directions = [
        (0,1), # Right
        (0,-1), # Left
        (-1,0), # Top
        (1,0) # Bottom
    ]
    def numIslands(self, grid: List[List[str]]) -> int:
        if(len(grid) == 0):
            return 0
        
        island_number = 0
        queue = list()

        for i, row in enumerate(grid):
            for j, column in enumerate(grid[0]):
                if(grid[i][j] == "1"):
                    grid[i][j] = "0"
                    island_number += 1
                    queue.append((i,j))
                    while(len(queue) > 0):
                        pos = queue.pop()
                        for direction in self.directions:
                            cur_i = pos[0] + direction[0]
                            cur_j = pos[1] + direction[1]
                            if cur_i >= 0 and cur_i < len(grid) and cur_j >= 0 and cur_j < len(grid[0]) and grid[cur_i][cur_j] == "1":
                                queue.append((cur_i,cur_j))
                                grid[cur_i][cur_j] = "0"
        return island_number
'''

# DFS
class Solution:
    directions = [
        (0,1), # Right
        (0,-1), # Left
        (-1,0), # Top
        (1,0) # Bottom
    ]
    def markCase(self, grid: List[List[str]], i: int, j: int):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == "0":
            return
        grid[i][j] = "0"
        for direction in self.directions:
            self.markCase(grid, i + direction[0], j + direction[1])

    def numIslands(self, grid: List[List[str]]) -> int:
        if(len(grid) == 0):
            return 0
        
        island_number = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    island_number += 1
                    self.markCase(grid, i, j)
        
        return island_number

grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]

solution = Solution()
print(solution.numIslands(grid))