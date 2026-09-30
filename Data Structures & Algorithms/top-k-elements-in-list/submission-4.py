from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums)==1 and k==1:
            return nums

        cnt = defaultdict(int)

        for i in nums:
            cnt[i] += 1

        # i,j = 0,len(nums)-1

        # while i<j:
        #     cnt[nums[i]] += 1
        #     cnt[nums[j]] += 1

        #     i+=1
        #     j-=1
        #     #for odd lenght
        #     if i==j:
        #         cnt[nums[i]] += 1
        
        sorted_cnt = dict(sorted(cnt.items(),key=lambda item:item[1],reverse=True))

        res = list(sorted_cnt.keys())[:k]
        return res