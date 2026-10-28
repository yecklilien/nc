class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = [False] * 25
        def traverse(idx, coms, visited):
            coms.append(nums[idx])
            visited[nums[idx]+10] = True

            if len(coms) == len(nums):
                res.append(coms.copy())

            for i in range(len(nums)):
                if not visited[nums[i] + 10]:
                    traverse(i, coms, visited)
            
            coms.pop()
            visited[nums[idx]+10] = False
        
        for i in range(len(nums)):
            traverse(i,[],visited)

        return res