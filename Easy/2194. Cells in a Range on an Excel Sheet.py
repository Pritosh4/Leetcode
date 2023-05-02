class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        row_end = int(s[-1])
        row_start = int(s[1])
        col_end = s[-2]
        col_start = s[0]
        col = ord(col_end) - ord(col_start)
        ans = []
        for i in range(col + 1):
            add = chr(i + ord(col_start))
            for j in range(row_start, row_end + 1):
                ans.append(add + str(j))
        return ans
