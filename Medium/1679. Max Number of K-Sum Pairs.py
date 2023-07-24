class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        '''
        nums.sort()
        i = 0
        j = len(nums) - 1
        ans = 0
        while i < j:
            tot = nums[i] + nums[j]
            if tot == k:
                ans+= 1
                i += 1
                j -= 1
            elif tot < k:
                i += 1
            else:
                j -= 1
        return ans
        '''    
        
        need = defaultdict(int)
        ans = 0
        for i in nums:
            if need[i] > 0:
                ans += 1
                need[i] -= 1
            else:
                need[k-i] += 1
        return ans
