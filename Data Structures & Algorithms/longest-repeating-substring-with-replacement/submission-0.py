class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l = r = max_count = 0
        counts = {}
        while (r < len(s)):
            if s[r] in counts:
                counts[s[r]] += 1
            else:
                counts[s[r]] = 1
            
            if counts[s[r]] > max_count:
                max_count = counts[s[r]]
        
            if r - l + 1 <= max_count + k:
                if r - l > res:
                    res = r - l
            else:
                while (r - l + 1> max_count + k):
                    counts[s[l]] -= 1
                    l+=1
            r += 1
                
        return res+1