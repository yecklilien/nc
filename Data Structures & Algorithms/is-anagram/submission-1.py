class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_char_dict = {}
        for char in s:
            if char in s_char_dict:
                s_char_dict[char] += 1
            else:
                s_char_dict[char] = 1
        
        for char in t:
            if char in s_char_dict and s_char_dict[char] > 0:
                s_char_dict[char] -= 1
            else:
                return False
        
        for char in s_char_dict:
            if s_char_dict[char] != 0:
                return False

        return True