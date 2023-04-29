class Solution:
    def sortSentence(self, s: str) -> str:
        s_list = s.split()
        ans = [''] * len(s_list)
        for i in s_list:
            ans[int(i[-1]) - 1] = i[:-1]
        return ' '.join(ans)
