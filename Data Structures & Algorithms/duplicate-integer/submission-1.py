class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counts = dict()
        l = len(nums)
        i=0
        j = l-1
        while i<j:
            ni = nums[i]
            nj=nums[j]
            counts[ni] = counts.get(ni,0) + 1
            if counts[ni]>1:
                return True
            counts[nj] = counts.get(nj,0) + 1
            if counts[nj]>1:
                return True
            i += 1
            j -= 1
            if i==j and (counts.get(nums[i],0) + 1)>1:
                return True
        return False
        # for i in nums:
        #     counts[i] = counts.get(i,0)+1
        #     if counts[i]>1:
        #         return True
        # return False