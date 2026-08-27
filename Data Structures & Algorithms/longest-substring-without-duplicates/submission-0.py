class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        r=0
        char_counter= [False] * 130
        result = 0
        length = len(s)
        while l<length and r<length:
            char_index = ord(s[r])
            if not char_counter[char_index]:
                char_counter[char_index] = True
                if r-l+1>result:
                    result = r-l+1
                r+=1
            else:
                char_counter[ord(s[l])] = False
                l+=1
        return result

