class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [-1] * (len(nums)+2)
        def dp(idx):
            if idx >= len(nums):
                memo[idx] = 0
            
            if memo[idx] != -1:
                return memo[idx]
            
            
            memo[idx] = max((dp(idx+2) + nums[idx]), dp(idx+1))
            return memo[idx]
        
        return dp(0)
