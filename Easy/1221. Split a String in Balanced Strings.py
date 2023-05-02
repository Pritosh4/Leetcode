class Solution:
    def balancedStringSplit(self, s: str) -> int:
        l, r = 0, 0
        count = 0
        for i in s:
            if i == 'R':
                r += 1
            else:
                l += 1
            
            if l == r:
                count += 1
                l, r = 0, 0
        return count
