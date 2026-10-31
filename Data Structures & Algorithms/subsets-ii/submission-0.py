class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        result = []
        def traverse(idx, subset):
            if idx >= len(nums):
                result.append(subset.copy())
                return

            # take
            subset.append(nums[idx])
            traverse(idx + 1, subset)
            subset.pop()

            #skip
            i = idx + 1
            while(i < len(nums) and nums[i] == nums[idx]):
                i+=1
            traverse(i, subset)
        
        traverse(0,[])
        return result
        