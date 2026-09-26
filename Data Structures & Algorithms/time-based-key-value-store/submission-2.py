class TimeMap:

    def __init__(self):
        self.key_dict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.key_dict:
            self.key_dict[key] = []
        self.key_dict[key].append((value,timestamp))


    def get(self, key: str, timestamp: int) -> str:
        if not key in self.key_dict:
            return ""

        values = self.key_dict[key]
        l = 0
        r = len(values) - 1
        #print(values)
        # i=0
        while (l<=r):
            # if i > 10:
            #     break
            # i+=1
            mid = (l+r)//2
            # print(l,r,mid)
            if values[mid][1] <= timestamp:
                l = mid + 1
            else:
                r = mid - 1
        
        if values[r][1] <= timestamp:
            return values[r][0]
        
        return ""
# 25
# 10 20 30
# l  m  r
#       lmr