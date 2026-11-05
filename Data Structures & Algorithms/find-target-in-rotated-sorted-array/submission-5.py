class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r= 0,len(nums)-1
        res = -1
        while l<=r:
            m = (l+r)//2
            val = nums[m]
            # print(l,r,m,val)
            
            if val==target:
                res=m
                break
            
            ## if val in left sorted section
            if nums[l]<=val:
                if target>val or target<nums[l]:
                    l= m+1
                elif target<val:
                    r = m-1 
            
            ## if val in right sorted portion(nums[l]>val)
            else:
                if target<val or target>nums[r]:
                    r=m-1
                elif target>val:
                    l = m+1

        
        return res
            


           
