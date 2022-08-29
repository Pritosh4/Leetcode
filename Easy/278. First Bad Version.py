# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        lo = 1
        hi = n
        while lo <= hi:
            mid = (lo + hi) // 2
            if n == 1 or isBadVersion(mid) == True and isBadVersion(mid-1) == False:
                return mid
            if isBadVersion(mid) == True:
                hi = mid - 1 
            elif isBadVersion(mid) == False:
                lo = mid + 1
