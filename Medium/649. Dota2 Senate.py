class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r_count = 0
        for i in senate:
            if i == 'R':
                r_count += 1
        d_count = len(senate) - r_count

        r_ban = 0
        d_ban = 0
        queue = deque(senate)

        while r_count and d_count:
            cur = queue.popleft()
            if cur == 'R':
                if r_ban:
                    r_ban -= 1
                    r_count -= 1
                else:
                    d_ban += 1
                    queue.append(cur)
            else:
                if d_ban:
                    d_ban -= 1
                    d_count -= 1
                else:
                    r_ban += 1
                    queue.append(cur)
        return 'Radiant' if r_count else 'Dire'
