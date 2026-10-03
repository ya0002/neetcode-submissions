class Solution:
    # def longestConsecutive(self, nums: List[int]) -> int:
    #     numSet = set(nums)
    #     longest = 0

    #     for num in numSet:
    #         if (num - 1) not in numSet:
    #             length = 1
    #             while (num + length) in numSet:
    #                 length += 1
    #             longest = max(length, longest)
    #     return longest
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        if len(nums)==1:
            return 1

        cons_cnt = 1
        prev_cons_cnt = 0
        sorted_nums = sorted(set(nums))
        print(sorted_nums)
        
        for i in range(1,len(sorted_nums)):
            cur = sorted_nums[i]
            prev = sorted_nums[i-1]
            if cur-prev==1 or (prev<0 and cur-prev==-1 ):
                cons_cnt += 1
            else:
                if cons_cnt>prev_cons_cnt:
                    prev_cons_cnt = cons_cnt
                cons_cnt = 1

        if prev_cons_cnt>cons_cnt:
            return prev_cons_cnt

        return cons_cnt