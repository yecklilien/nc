class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        combs = []
        com_sum = 0
        def take(idx):
            nonlocal com_sum
            if com_sum > target or idx >= len(nums):
                return
            if com_sum == target:
                res.append(combs.copy())
                return
            #take
            combs.append(nums[idx])
            com_sum += nums[idx]
            take(idx)
            combs.pop()
            com_sum -= nums[idx]
            take(idx+1)
        take(0)
        return res
        