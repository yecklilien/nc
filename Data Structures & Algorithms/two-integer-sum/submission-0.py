class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        number_dict = {}
        for i in range(len(nums)):
            if nums[i] in number_dict:
                number_dict[nums[i]].append(i)
            else:
                number_dict[nums[i]] = [i]
        
        for i in range(len(nums)):
            left = target - nums[i]
            if left in number_dict:
                for index in number_dict[left]:
                    if index == i:
                        continue
                    return [i, index] 
        
        return []