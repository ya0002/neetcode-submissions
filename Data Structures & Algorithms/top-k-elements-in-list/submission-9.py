from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums)==1 and k==1:
            return nums

        cnt = defaultdict(int)

        for i in nums:
            cnt[i] += 1
        
        # sorted_cnt = dict(sorted(cnt.items(),key=lambda item:item[1],reverse=True))

        # res = list(sorted_cnt.keys())[:k]

        heap =[]
        for num,freq in cnt.items():
            # smaller the frequency(v), higher the priority
            heapq.heappush(heap,(freq,num))
            if len(heap)>k:
                # pop the element with the smallest frequency(highest priority)
                heapq.heappop(heap)
        
        
        res =[]
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])## pop and only keep the actual value from num, not thhe frequency
        
        return res