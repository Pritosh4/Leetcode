class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        # If the number is out of bounds
        if target >= letters[len(letters)-1] or target < letters[0]:
            return letters[0]
        
        lo = 0
        hi = len(letters) - 1
        while lo <= hi:
            mid =(lo + hi) // 2
            if letters[mid] > target and  letters[mid-1] <= target:
                return letters[mid]
            elif letters[mid] <= target:
                lo = mid + 1
            else:
                hi = mid - 1
