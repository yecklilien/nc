class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result_dict = {}
        for string in strs:
            hashed = self.hashString(string)
            if hashed in result_dict:
                result_dict[hashed].append(string)
            else:
                result_dict[hashed] = [string]

        result = []
        for hashed in result_dict:
            result.append(result_dict[hashed])
        
        return result

    def hashString(self, string: str) -> tuple:
        result = [0]*26
        for char in string:
            result[ord(char)-ord('a')] += 1
        return tuple(result)