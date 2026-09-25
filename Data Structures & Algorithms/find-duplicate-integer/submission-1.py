class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0
        while(nums[slow] != nums[nums[fast]]):
            slow = nums[slow]
            fast = nums[nums[fast]]
            
        slow = nums[slow]
        slow2 = 0
        while(nums[slow2] != nums[slow]):
            slow = nums[slow]
            slow2 = nums[slow2]

        return nums[slow]
