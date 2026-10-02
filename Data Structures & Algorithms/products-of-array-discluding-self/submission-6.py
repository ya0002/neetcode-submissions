class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l_nums = len(nums)
        zero_cnt = 0
        for num in nums:
            if num==0:
                zero_cnt +=1
            if zero_cnt>1:
                return [0]*l_nums

        
        prefix = [1]*l_nums
        postfix = [1]*l_nums
        res = [None]*l_nums

        i,j = 1, l_nums-2 ## i is for prefix and j for postfix

        current_pre,current_post =1,1
        while j>=0:
            current_pre *= nums[i-1]
            prefix[i] = current_pre

            current_post *= nums[j+1]
            postfix[j] = current_post

            ## when i crosses j, we start building the result
            if i>=j:
                res[i] = prefix[i]*postfix[i]
                res[j] = prefix[j]*postfix[j]

            i+=1
            j-=1

        return res

        # prd=defaultdict(lambda: 1)
        # # prd_b=defaultdict(lambda: 1)
        # for i in range(len(nums)):
        #     prd[i] = 1
        #     for k in prd.keys():
        #         if i!=k:
        #             prd[k] *= nums[i]
        #             prd[i] *= nums[k] 
                    
        # return list(prd.values())