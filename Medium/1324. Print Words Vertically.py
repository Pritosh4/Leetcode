class Solution:
    def printVertically(self, s: str) -> List[str]:
        sl = s.split()
        length = len(sl)
        
        word_len = 0
        for i in sl:
            word_len = max(word_len, len(i))
        ans = [''] * word_len
        for j in range(word_len):
            for k in sl:
                if j >= len(k):
                    ans[j] += ' ' 
                else:
                    ans[j] += k[j]
        for i in range(len(ans)):
            ans[i] = ans[i].rstrip()
        return ans
