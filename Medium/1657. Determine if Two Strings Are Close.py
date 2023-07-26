class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        hash1 = {}
        hash2 = {}
        for i in word1:
            if i in hash1:
                hash1[i] += 1
            else:
                hash1[i] = 1
        
        for j in word2:
            if j in hash2:
                hash2[j] += 1
            else:
                hash2[j] = 1
        
        return set(word1) == set(word2) and sorted(hash1.values()) == sorted(hash2.values()) 
