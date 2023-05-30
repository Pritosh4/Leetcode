class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        maxcount, row = 0, 0
        for i in range(len(mat)):
            count = 0
            for j in mat[i]:
                if j == 1:
                    count += 1
            if count > maxcount:
                maxcount = count
                row = i
        return [row, maxcount]
