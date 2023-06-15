class Solution:
    def maxDepth(self, s: str) -> int:
        ans, count = 0, 0
        for i in range(len(s)):
            if s[i] == '(':
                count += 1
                ans = max(ans, count)
            elif s[i] == ')':
                count -= 1
        return ans
