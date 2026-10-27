class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        def traverse(idx, subset, total):
            if total == target:
                result.append(subset.copy())
                return
            if total > target or idx >= len(candidates):
                return
            
            #Take
            subset.append(candidates[idx])
            traverse(idx+1, subset, total + candidates[idx])
            subset.pop()

            #Skip
            i = idx
            while (i < len(candidates) and candidates[i] == candidates[idx]):
                i+=1
            traverse(i, subset, total)
        
        traverse(0,[],0)
        return result
        