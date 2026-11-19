import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        klosest=[]

        for p in points:

            d = math.sqrt(p[0]**2 + p[1]**2)
            heapq.heappush(klosest,(d,p))
        
        print(klosest)
        res=[]
        while k:
            priority, p = heapq.heappop(klosest)
            res.append(p)
            k-=1
        return res
