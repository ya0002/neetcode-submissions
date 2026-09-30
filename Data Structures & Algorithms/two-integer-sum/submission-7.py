class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            e = nums[i]
            diff = target - e
            if diff in nums[i+1:]:
                j = nums.index(diff,i+1)
                if i!=j:
                    return [i,j]
        