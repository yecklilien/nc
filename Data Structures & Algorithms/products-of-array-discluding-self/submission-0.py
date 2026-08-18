class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_prefix = [None] * len(nums)
        for i in range (len(nums)):
            if i == 0:
                left_prefix[i] = nums[i]
            else:
                left_prefix[i] = left_prefix[i-1]*nums[i]
        
        right_prefix = [None] * len(nums)
        for i in reversed(range(len(nums))):
            if i == len(nums)-1:
                right_prefix[i] = nums[i]
            else:
                right_prefix[i] = right_prefix[i+1] * nums[i]

        result = []
        for i in range (len(nums)):
            l = i - 1
            r = i + 1
            res = 1
            if l >= 0:
                res *= left_prefix[l]
            if r < len(nums):
                res *= right_prefix[r]
            result.append(res)
        return result