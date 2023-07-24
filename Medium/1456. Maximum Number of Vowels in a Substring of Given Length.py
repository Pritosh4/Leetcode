class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        sub = s[:k]
        vow = {'a', 'e', 'i', 'o','u'}
        vows = 0
        for i in sub:
            if i in vow:
                vows += 1
        ans = vows
        for i in range(k, len(s)):
            if s[i] in vow:
                vows += 1
            if s[i - k] in vow:
                vows -= 1
            ans = max(ans, vows)
        return ans
