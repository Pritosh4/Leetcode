class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        freq = collections.defaultdict(int)
        count = 0
        for i in range(len(arr)):
            rem  = k - (arr[i] % k)
            if rem in freq and freq[rem] >= 1:
                count += 1
                freq[rem] -= 1
            else:
                if arr[i] % k == 0:
                    freq[k] += 1
                else:
                    freq[arr[i] % k] += 1
        return count == len(arr) // 2
