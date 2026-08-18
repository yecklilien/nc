class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        has_appear = {}
        for number in nums:
            if number in has_appear:
                return True
            else:
                has_appear[number] = True
        return False