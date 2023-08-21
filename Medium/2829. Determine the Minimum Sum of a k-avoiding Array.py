class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        no = set()
        tot = 0
        i = 1
        while n != 0:
            if i not in no:
                tot += i
                no.add(k - i)
                n -= 1
            i += 1
        return tot
