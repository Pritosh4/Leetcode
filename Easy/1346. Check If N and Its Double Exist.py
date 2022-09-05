class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr.sort()
        for i in range(len(arr)):
            if arr[i] >= 0:
                low = i + 1
                high = len(arr) - 1
                while low <= high:
                    mid = (low + high) // 2
                    if arr[mid] == arr[i] * 2:
                        return True
                    elif arr[i] * 2 > arr[mid]:
                        low = mid + 1
                    else:
                        high = mid - 1
            else:
                low = 0
                high = i
                while low <= high:
                    mid = (low + high) // 2
                    if arr[mid] == arr[i] * 2:
                        return True
                    elif arr[i] * 2 > arr[mid]:
                        low = mid + 1
                    else:
                        high = mid - 1            
        return False 
        
