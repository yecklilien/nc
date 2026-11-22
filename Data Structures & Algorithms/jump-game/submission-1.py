class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxreach = 0
        i = 0
        while (i<len(nums) and i <= maxreach):
            maxreach = max(maxreach, i + nums[i])
            print(maxreach)
            i+=1
        
        if maxreach >= len(nums)-1:
            return True

        return False
             