class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for i in s:
            if i == '(':
                stack.append(i)
            else:
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(i)
        return len(stack) 

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        bal = 0
        count = 0
        for i in s:
            if i == '(':
                bal += 1
            else:
                if bal == 0:
                    count += 1
                else:
                    bal -= 1
        return count + bal
