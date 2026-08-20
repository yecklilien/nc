class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max = 0
        for pile in piles:
            if max < pile:
                max = pile
        
        l=1
        r=max

        while l<=r:
            mid = l+((r-l)//2)
            time = self.totalTimeTaken(piles, mid)
            if time > h: #mid to small
                l=mid+1
            else:
                #mid below range
                r=mid-1
        return l

    
    def totalTimeTaken(self, piles: List[int], amount: int) -> int:
        result = 0
        for i in range(len(piles)):
            result += piles[i]//amount
            if piles[i]%amount != 0:
                result +=1
        return result



        