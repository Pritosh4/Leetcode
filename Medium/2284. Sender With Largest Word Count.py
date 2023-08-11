class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        freq = defaultdict(int)
        for i in range(len(messages)):
            count = 0
            for j in messages[i]:
                if j == ' ':
                    count += 1
            freq[senders[i]] += count + 1
        max_val = 0
        for i in freq:
            if freq[i] > max_val:
                max_val = freq[i]
                ans = i
            elif freq[i] == max_val:
                if i > ans:
                    ans = i
        return ans
