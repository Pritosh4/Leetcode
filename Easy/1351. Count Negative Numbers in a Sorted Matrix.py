class Solution:
    def binarysearch(self, row):
        low = 0
        high = len(row) - 1
        while low <= high:
            mid = (low + high) // 2
            if row[mid] < 0:
                high = mid - 1
            else:
                low = mid + 1
        return len(row) - low
    
    
    
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for row in grid:
            count += self.binarysearch(row)
        return count
        
