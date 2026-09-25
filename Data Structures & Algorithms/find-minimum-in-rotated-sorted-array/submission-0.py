class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        if nums[l] < nums[r]:
            return nums[l]

        while l < r:
            mid = (l + r) // 2
            print(l, r, mid)
            if nums[mid] < nums[r]:
                r = mid
            elif nums[mid] >= nums[r]:
                l = mid + 1
            #print(l, r)
        return nums[l]

# 0 1 2 3 4 5
# 3 4 5 6 1 2