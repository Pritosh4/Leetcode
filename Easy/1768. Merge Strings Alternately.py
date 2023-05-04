class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1 = len(word1)
        len2 = len(word2)
        ans = ''
        for i in range(min(len1, len2)):
            ans += word1[i]
            ans += word2[i] 
        if len1 > len2:
            ans += word1[i+1:]
        else:
            ans += word2[i+1:]
        return ans
