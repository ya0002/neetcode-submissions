class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = dict()
        for i in range(len(nums)):
            e = nums[i]
            diff[i] = target - e
            if diff[i] in nums[i+1:]:
                j = nums.index(diff[i],i+1)
                if i!=j:
                    return [i,j]
        