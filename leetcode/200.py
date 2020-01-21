class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) < 1:
            return 0
        islands = 0
        height = len(grid)
        width = len(grid[0])

        for row in range(height):
            for column in range(width):
                if grid[row][column] == '1':
                    islands += 1
                    self.dfs(grid, row, column)

        return islands

    def dfs(self, grid, row, column):
        min_row = 0
        max_row = len(grid) - 1
        min_column = 0
        max_column = len(grid[0]) - 1

        if (not min_row <= row <= max_row) or (not min_column <= column <= max_column):
            return
        elif grid[row][column] == '0':
            return
        else:
            grid[row][column] = '0'
            self.dfs(grid, row - 1, column)
            self.dfs(grid, row + 1, column)
            self.dfs(grid, row, column - 1)
            self.dfs(grid, row, column + 1)