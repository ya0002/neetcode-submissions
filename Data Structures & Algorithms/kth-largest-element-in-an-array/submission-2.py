import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
       
        nums2 = []
        for i in nums:
            nums2.append([-i,i])
        heapq.heapify(nums2)
        # print(nums2)
        res = None
        while k:
            p,res = heapq.heappop(nums2)
            k-=1
        return res