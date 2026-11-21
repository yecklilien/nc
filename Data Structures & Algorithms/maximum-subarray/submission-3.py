class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = 0
        max = -10005
        for num in nums:
            sum += num
            if sum > max:
                max = sum
            if sum < 0:
                sum = 0
        return max
        