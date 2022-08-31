class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            remaining = target - numbers[i]
            low = i + 1
            high = len(numbers) - 1
            while low <= high:
                mid = (low + high) // 2
                if remaining == numbers[mid]:
                    return [i + 1, mid + 1]
                elif remaining > numbers[mid]:
                    low = mid + 1
                elif remaining < numbers[mid]:
                    high = mid - 1
            
