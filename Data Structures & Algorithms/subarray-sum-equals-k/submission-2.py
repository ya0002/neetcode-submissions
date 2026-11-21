class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prev_sum = {0:1}

        total,cnt=0,0
        
        for i in nums:
            total += i
            diff = total-k#If diff has appeared as a prefix sum before, then every time it appeared marks the start of a valid subarray ending at the current index.
            cnt += prev_sum.get(diff, 0)
            prev_sum[total] = prev_sum.get(total,0) + 1

        return cnt