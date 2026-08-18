class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        num_dict = defaultdict(lambda:-1)
        max = 0
        for num in num_set:
            if num_dict[num] != -1:
                continue

            curr = num
            while curr + 1 in num_set:
                if num_dict[curr + 1] != -1:
                    curr += num_dict[curr + 1]
                    break
                else:
                    num_dict[curr] = 1
                    curr+=1
            num_dict[num] = curr-num+1
            if num_dict[num] > max:
                max = num_dict[num]
        return max
