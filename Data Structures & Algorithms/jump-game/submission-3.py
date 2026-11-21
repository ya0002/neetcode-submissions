class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums)-1

        for i in range(len(nums)-2,-1,-1):
            if nums[i]>=(goal-i):
                goal=i
            print(i,goal)
            
        return goal==0

        # i = 0

        # while i<len(nums)-1:
        #     if not nums[i]:
        #         return False
        #     if nums[i+1]>nums[i]:
        #         i+=1
        #     else:
        #         i += nums[i]
        
        # return True
        