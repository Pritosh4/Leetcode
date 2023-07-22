class Solution:
    def reverseVowels(self, s: str) -> str:
        ans = list(s)
        vow = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        i = 0
        j = len(ans) - 1
        while i <= j:
            if ans[i] in vow and ans[j] in vow:
                ans[i], ans[j] = ans[j], ans[i]
                i += 1
                j -= 1
            elif ans[i] not in vow:
                i += 1
            elif ans[j] not in vow:
                j -= 1
            
                
        return ''.join(ans)
