class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        t = 0
        ans = []
        count = 0
        for i in range(1, n + 1):
            if i == target[t]:
                count += 1
                ans.append('Push')
                t += 1
            else:
                ans.extend(['Push', 'Pop'])
            if count == len(target):
                break
        return ans
