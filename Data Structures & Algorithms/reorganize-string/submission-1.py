import heapq
from collections import Counter
class Solution:
    def reorganizeString(self, s: str) -> str:

        smap = Counter(s)

        maxHeap = []
        for c,cnt in smap.items():
            heapq.heappush(maxHeap,(-cnt,c)) 

        res = ""
        cnt,c = heapq.heappop(maxHeap)
        while maxHeap:
            # if res and res[-1]==c:
            #     print(res)
            #     return ""
            res += c
            cnt2,c2 = heapq.heappop(maxHeap)
            if cnt+1:
                heapq.heappush(maxHeap,(cnt+1,c))
            cnt,c = cnt2,c2

        res += c

        if len(res)!=len(s):
            return ""

        return res

        