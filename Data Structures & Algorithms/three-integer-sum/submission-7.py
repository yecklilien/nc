class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i!=0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = len(nums)-1
            while(l<r):
                if l != i+1 and nums[l] == nums[l-1]:
                    l+=1
                elif -nums[i] == nums[l] + nums[r]:
                    result.append([nums[i], nums[l], nums[r]])
                    l+=1
                elif -nums[i] < nums[l] + nums[r]:
                    r-=1
                elif -nums[i] > nums[l] + nums[r]:
                    l+=1 
        return result
