class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        words = 0
        for i in sentences:
            words = max(len(i.split()), words)
        return words
