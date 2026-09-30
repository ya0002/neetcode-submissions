class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counts = dict()
        for i in nums:
            counts[i] = counts.get(i,0)+1
            if counts[i]>1:
                return True
        return False