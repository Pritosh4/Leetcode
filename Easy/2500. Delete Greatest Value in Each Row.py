class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for i in grid:
            i.sort()
        
        maxi, ans = 0, 0
        for i in range(len(grid[0])):
            for j in range(len(grid)):
                maxi = max(maxi, grid[j][i])
            ans += maxi
        return ans
      
