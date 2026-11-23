class Solution:
    def climbStairs(self, n: int) -> int:
        
        if not n:
            return 0
        if n==1:
            return 1

        last=1
        res=1
        
        # res += last
        
        for i in range(n-1):
            temp = res
            res += last 
            last=temp

        return res