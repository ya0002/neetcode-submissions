from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.db = defaultdict(lambda: defaultdict(list))
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.db[key]["v"].append(value)
        self.db[key]["ts"].append(timestamp)

        

    def get(self, key: str, timestamp: int) -> str:
        k_store=self.db[key]
        
        k_ts = k_store["ts"]
        l,r = 0,len(k_ts)-1

        res=""

        while l<=r:

            m = (l+r)//2
            val = k_ts[m]
            
            if val==timestamp:
                return k_store["v"][m]

            if val>timestamp:
                r = m-1
            else:
                l= m+1
                res = k_store["v"][m]
        
        return res
        
