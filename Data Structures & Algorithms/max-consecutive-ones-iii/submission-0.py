class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        bits_cnt={0:0,1:0}

        l,r=0,0
        res = 0

        while l<=r and r<len(nums):
            cur = nums[r]
            bits_cnt[cur] += 1
            # print(bits_cnt)

            if bits_cnt[0]>k:
                bits_cnt[nums[l]] -= 1
                l+=1
                
            else:
                res = max(res,bits_cnt[0]+bits_cnt[1])
                
            r+=1
        
        return res