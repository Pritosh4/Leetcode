class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append([s[i], i])
            elif s[i] == ')':
                if stack and stack[-1][0] == '(':
                    stack.pop()
                else:
                    stack.append([s[i], i])
        ans = list(s)
        for i in stack:
            ans[i[1]] = ''
        return ''.join(ans)
