class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        ans = ''
        start = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(s[i])
            elif s[i] == ')':
                stack.pop()
            if not stack:
                ans += s[start + 1:i]
                start = i + 1
        return ans
