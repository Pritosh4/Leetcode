# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 1
        high = n
        while low <= high:
            mid = (low + high) // 2
			# If n is 1 then we have to return that as the bad version else we check to see 
			# if the current mid version is a bad version and the version before is not a bad version.
            if n == 1 or isBadVersion(mid) == True and isBadVersion(mid-1) == False:  
                return mid
            if isBadVersion(mid) == True: # If true then the first bad version lies on the left of mid
                hi = mid - 1 
            elif isBadVersion(mid) == False: # If false then the first bad version lies on the right of mid
                lo = mid + 1
