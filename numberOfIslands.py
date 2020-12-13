class Solution:
    def numIslands(self, grid):
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if(grid[i][j] == '1'):
                    count = count + 1
                    self.dfs(grid, i, j)

        return count

    def dfs(self, grid, i, j):
        if(i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] == '0'):
            return

        grid[i][j] = '0'
        self.dfs(grid, i-1, j)  # up
        self.dfs(grid, i+1, j)  # down
        self.dfs(grid, i, j-1)  # left
        self.dfs(grid, i, j+1)  # right


grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]

print(Solution().numIslands(grid))
