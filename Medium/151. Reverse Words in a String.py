class Solution:
    def reverseWords(self, s: str) -> str:
        ans = []
        temp = ''
        for c in s:
            if c != ' ':
                temp += c
            elif temp != '':
                ans.append(temp)
                temp = ''
        if temp != '':
            ans.append(temp)
            
        return ' '.join(ans[::-1])
