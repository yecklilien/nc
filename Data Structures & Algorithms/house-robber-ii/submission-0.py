class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def dorob(nums):
            twoprev, prev = 0, 0 
            for num in (nums):
                curr = max(twoprev + num, prev)
                twoprev = prev
                prev = curr
            
            return prev

        return max(nums[0], dorob(nums[1:]), dorob(nums[:-1]))
        
    

