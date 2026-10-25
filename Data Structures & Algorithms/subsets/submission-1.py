class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []
        def traverse (idx):
            if idx == len(nums):
                result.append(subset.copy())
                return
            
            subset.append(nums[idx])
            traverse(idx + 1)
            subset.pop()
            traverse(idx + 1)
        
        traverse(0)
        return result