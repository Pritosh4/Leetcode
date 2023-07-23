class Solution:
    def compress(self, chars: List[str]) -> int:
        ans = 0
        count = 1
        i = 0
        while i < len(chars):
            while i + count < len(chars) and chars[i + count] == chars[i]:
                count += 1
            chars[ans] = chars[i]
            ans += 1
            i += count
            if count > 1:
                count = str(count)
                chars[ans:ans + len(count)] = list(count)
                ans += len(count)
                count = 0 
        return ans
