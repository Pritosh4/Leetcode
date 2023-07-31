class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        ans = 0
        while a or b or c:
            if c & 1 == 1:
                if a & 1 == 1:
                    pass
                elif b & 1 == 1:
                    pass
                else:
                    ans += 1
            else:
                if a & 1 == 1:
                    ans += 1
                if b & 1 == 1:
                    ans += 1

            c = c >> 1
            a = a >> 1
            b = b >> 1
        return ans
