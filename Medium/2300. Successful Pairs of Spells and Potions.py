class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        ans = []
        potions.sort()
        m = len(potions)
        max_potion = potions[m - 1]
        for i in spells:
            min_potion = ceil(success/i)
            if min_potion > max_potion:
                ans.append(0)
            else:
                lo = 0
                hi = m
                while lo < hi:
                    mid = (lo + hi) // 2
                    if potions[mid] >= min_potion:
                        hi = mid
                    else:
                        lo = mid + 1
                ans.append(m - lo)
        return ans
                        
