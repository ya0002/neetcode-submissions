import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        ## no need for the list since these are contin. values,mid+1
        # poss = list(range(1,max(piles)))
        

        l,r=0,max(piles)-1
        res = max(piles)

        while l<=r:
            m = (l+r)//2
            rate = m+1 #poss[m]
            

            ## check if the rate is valid
            req_h= 0
            for pile in piles:
                req_h += math.ceil(pile/rate) ## eg= 6/4 = 1.5 -> 2 hrs
            
            if req_h<=h:
                res = min(res,rate)
                r= m-1
            elif req_h>h:
                l = m+1
        
        return res
        