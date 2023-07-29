class Solution:
    def decodeString(self, s: str) -> str:
        ans = ''
        stack = []
        k = 0
        for i in s:
            if i == '[':
                stack.append([ans, k])
                ans = ''
                k = 0
            elif i == ']':
                last_ans, last_k = stack.pop()
                ans = last_ans + last_k*ans
            elif i.isdigit():
                k = k * 10 + int(i)
            else:
                ans += i
        return ans



                
