class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = 0
        for i in ransomNote:
            if i not in magazine:
                return False
            
            magazine = magazine.replace(i, '',1)
        return True
