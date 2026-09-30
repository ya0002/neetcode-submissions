class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val_id= {val:idx for idx,val in enumerate(nums)}
        
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in val_id and i!=val_id[diff]:
                
                return [i,val_id[diff]]
        