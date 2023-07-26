class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        freq = {}
        count = 0
        for i in grid:
            freq[tuple(i)] = freq.get(tuple(i), 0) + 1
        
        for c in range(len(grid[0])):
            col = []
            for r in range(len(grid)):
                col.append(grid[r][c])
            if tuple(col) in freq:
                count += freq[tuple(col)]
        return count
