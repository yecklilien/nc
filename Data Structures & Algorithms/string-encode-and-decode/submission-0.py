class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for string in strs:
            result += str(len(string))
            result += '#'
            result += string
        print(result)
        return result

    def decode(self, s: str) -> List[str]:
        length = ''
        i = 0
        result = []
        while i < len(s):
            if s[i] != '#':
                length += s[i]
                i+=1
            else:
                i+=1
                actlen = int(length)
                string = ''
                for j in range(i,i+actlen,1):
                    string+=s[j]
                result.append(string)
                i+=actlen
                length = ''
        return result