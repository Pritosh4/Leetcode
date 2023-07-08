class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        freq = [0] * 10
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                freq[int(secret[i])] += 1
                freq[int(guess[i])] -= 1
        
        tot = 0
        for i in freq:
            if i > 0:
                tot += i
        return f'{bulls}A{len(secret) - bulls - tot}B' 

            
        
