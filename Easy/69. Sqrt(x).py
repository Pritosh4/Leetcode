class Solution:
    def mySqrt(self, x: int) -> int:
        lo,hi=0,1+(x//2)
        while lo<=hi:
            mid=(lo+hi)//2
            if mid*mid<=x<(mid+1)*(mid+1):
                return mid
            elif mid*mid>x:
                hi=mid-1
            else:
                lo=mid+1
