class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freq = defaultdict(int)
        for num in nums:
            num_freq[num] += 1
        
        freq_bucket = [[] for _ in range (len(nums) + 1)]

        for num in num_freq:
            freq_bucket[num_freq[num]].append(num)
        
        result = []
        count = k
        for freq in reversed(range(len(nums) + 1)):
            if len(freq_bucket[freq]) > 0:
                result.extend(freq_bucket[freq][:count])
                count -= len(freq_bucket[freq])

            if count <=0:
                break
        
        return result
