class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        R = len(matrix)
        C = len(matrix[0])
        for i in range(R):
            for j in range(i,C):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                
        for i in range(R):
            for j in range(C//2):
                matrix[i][j], matrix[i][C-j-1] = matrix[i][C-j-1], matrix[i][j]
