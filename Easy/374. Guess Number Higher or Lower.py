class Solution:
    def guessNumber(self, n: int) -> int:
        low = 1
        hi = n
        while low <= hi:
            mid = (hi + low)//2
            if guess(mid) == 0:
                return mid
            elif guess(mid) == 1:
                low = mid + 1
            elif guess(mid) == -1:
                hi = mid - 1
