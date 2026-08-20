class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] != i:
                temp = nums[i]
                nums[i] = -1
                while temp >= 0 and temp <= len(nums)-1:
                    if nums[temp] == temp:
                        break

                    temp2 = nums[temp]
                    nums[temp] = temp
                    temp = temp2
        
        for i in range(len(nums)):
            if nums[i] == -1:
                return i
        
        print(nums)
        
        return len(nums)
                    