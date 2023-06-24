class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        ans = [0] * len(deck)
        deque = [i for i in range(len(deck))]
        deck.sort()
        for card in deck:
            ans[deque.pop(0)] = card
            if deque:
                deque.append(deque.pop(0))
        return ans
