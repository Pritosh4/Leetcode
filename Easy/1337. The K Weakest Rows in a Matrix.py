class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        solution = []
        for i in range(len(mat)):
            low = 0
            high = len(mat[i]) - 1
            while low <= high:
                mid = (low + high) // 2
                if mat[i][mid] == 0:
                    high = mid - 1
                else:
                    low = mid + 1
            solution.append(high + 1)
            
               
        final_solution = []
        for i in sorted(solution):
            final_solution.append(solution.index(i))
            x = solution.index(i) 
            solution[x] = None
            
            
        return final_solution[:k]
