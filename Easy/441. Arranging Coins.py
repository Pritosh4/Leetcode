# The problem can be reformulated as follows:

# Find the maximum k such that  (k(k+1))/2 <= N.

class Solution:
    def arrangeCoins(self, n: int) -> int:
        lo = 0
        hi = n
        while lo <= hi:
            k = (lo + hi) // 2
            value = (k*(k + 1)) / 2
            if value == n:
                return k
            elif value > n:
                hi = k - 1
            elif value < n:
                lo = k + 1
        return hi
            
