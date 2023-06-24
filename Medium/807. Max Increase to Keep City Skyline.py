class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        row_max = []
        for row in grid:
            row_max.append(max(row))
        
        col_max = []
        for col in range(len(grid[0])):
            max_col = 0
            for row in range(len(grid)):
                max_col = max(max_col, grid[row][col])
            col_max.append(max_col)

        ans = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                ans += min(row_max[row], col_max[col]) - grid[row][col]
        return ans
