# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        lo = 0
        hi = mountain_arr.length() - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                lo = mid + 1
            else:
                hi = mid
        peak = lo

        lo = 0
        hi = peak
        while lo <= hi:
            mid = (lo + hi) // 2
            if mountain_arr.get(mid) == target:
                return mid
            elif mountain_arr.get(mid) > target:
                hi = mid - 1
            else:
                lo = mid + 1

        lo = peak
        hi = mountain_arr.length() - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if mountain_arr.get(mid) == target:
                return mid
            elif mountain_arr.get(mid) > target:
                lo = mid + 1
            else:
                hi = mid - 1
        
        return -1
