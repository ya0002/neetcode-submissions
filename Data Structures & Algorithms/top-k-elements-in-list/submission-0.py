from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = defaultdict(int)

        for i in nums:
            cnt[i] += 1
        
        sorted_cnt = dict(sorted(cnt.items(),key=lambda item:item[1],reverse=True))

        res = list(sorted_cnt.keys())[:k]
        return res