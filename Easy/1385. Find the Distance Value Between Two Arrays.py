class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        count = 0
        for i in arr1:
            lo = 0
            hi = len(arr2) - 1
            while lo <= hi:
                mid = (lo + hi)//2
                if abs(i-arr2[mid]) <= d:
                    count -= 1
                    break
                elif arr2[mid] > i:
                    hi = mid - 1
                else:
                    lo = mid + 1
            count += 1
        return count
                
