class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        def traverse(idx, subset):
            if idx >= len(nums):
                result.append(subset.copy())
                return
            
            subset.append(nums[idx])
            traverse(idx + 1, subset)
            subset.pop()
            traverse(idx + 1, subset)
        
        traverse(0, [])
        return result
        