class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = {}
        for i in arr:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        ans = []
        for i in freq.keys():
            ans.append(freq[i])
        return len(ans) == len(set(ans))
