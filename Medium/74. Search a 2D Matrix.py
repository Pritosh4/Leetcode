class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        col = len(matrix[0])
        row = len(matrix)
        low = 0
        high = col*row - 1
        while low<=high:
            mid = (high+low)//2
            if matrix[mid//col][mid%col]==target:
                return True
            elif matrix[mid//col][mid%col]>target:
                high = mid - 1
            elif matrix[mid//col][mid%col]<target:
                low = mid + 1
        return False
