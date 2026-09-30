class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        indices = {}  # val -> index

        for i, n in enumerate(nums):
            indices[n] = i

        for i, n in enumerate(nums):
            diff = target - n
            if diff in indices and indices[diff] != i:
                return [i, indices[diff]]
        return []
        # for i in range(len(nums)):
        #     diff = target - nums[i]
        #     if diff in nums[i+1:]:
        #         j = nums.index(diff,i+1)
        #         if i!=j:
        #             return [i,j]
        