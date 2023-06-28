class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i in ('+', '-', '*', '/'):
                ele2 = stack.pop()
                ele1 = stack.pop()
                if i == '+':
                    stack.append(ele1 + ele2)
                elif i == '-':
                    stack.append(ele1 - ele2)
                elif i == '*':
                    stack.append(ele1 * ele2)
                elif i == '/':
                    stack.append(math.trunc(ele1 / ele2))     
            else:
                stack.append(int(i))
        return stack.pop()
