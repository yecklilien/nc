class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        memo = [0] * (len(nums) + 1)
        memo[1] = nums[0]
        memo[2] = nums[1]

        for i in range(2,(len(nums)+1)):
            memo[i]= max(memo[i-2]+nums[i-1], memo[i-1])
        
        return max(memo[len(nums)],memo[len(nums)-1])