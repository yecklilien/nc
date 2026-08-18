class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_frequency = defaultdict(int)
        for num in nums:
            dict_frequency[num] += 1
        
        max_heap = []
        heapq.heapify_max(max_heap)
        for key in dict_frequency:
            heapq.heappush_max(max_heap, (dict_frequency[key], key))
        

        result = []
        for _ in range(k):
            top = heapq.heappop_max(max_heap)
            result.append(top[1])

        return result