class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        seen = set()
        for i in words:
            code = ''
            for j in i:
                code += morse[ord(j) - ord('a')]
            seen.add(code)
        return len(seen)
