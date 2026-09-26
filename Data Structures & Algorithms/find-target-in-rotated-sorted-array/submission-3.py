class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0 
        r = len(nums)-1
        while (l<=r):
            mid = (l+r) // 2
            print (l, r, (l+r)//2)
            if nums[mid] == target:
                return (l+r)//2
                break
            elif target < nums[mid]:
                if nums[l] <= target or nums[l] > nums[mid] : 
                    r = mid - 1
                else:
                    l = mid + 1 
            else:
                if nums[r] >= target or nums[r] < nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1
# 0 1 2 3 4 5
# 3 4 5 6 1 2
# l   m     r
