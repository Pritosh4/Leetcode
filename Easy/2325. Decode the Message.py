class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        seen = {}
        val = ord('a')
        for i in key:
            if i in seen or i == ' ':
                continue
            else:
                seen[i] = chr(val)
                val += 1
        ans = ''
        for i in message:
            if i == ' ':
                ans += ' '
            else:
                ans += seen[i]
        return ans
