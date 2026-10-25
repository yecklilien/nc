class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count_dict = {}
        for char in s1:
            if char not in count_dict:
                count_dict[char] = 0
            count_dict[char] += 1

        l = r = 0
        while (r < len(s2)):
            print(count_dict)
            print(l, r)
            char = s2[r]
            if char not in count_dict or count_dict[char] == 0:
                if s2[l] in count_dict:
                    count_dict[s2[l]] += 1
                l += 1
            else:
                count_dict[s2[r]] -= 1
                if r - l + 1 == len(s1):
                    return True
                r += 1
            
            if r < l:
                r+=1
        return False
            