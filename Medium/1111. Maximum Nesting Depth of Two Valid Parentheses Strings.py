class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        ans = []
        depth = 0
        for i in seq:
            if i == '(':
                depth += 1
            ans.append(depth % 2)
            if i == ')':
                depth -= 1
        return ans
