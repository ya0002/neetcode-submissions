class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        seen = set()
        res=0

        l,r=0,0

        while r<len(s):
            
            c=s[r]

            while c in seen:
                seen.remove(s[l])
                l+=1
                
                    
            
            seen.add(c)
            res=max(r-l+1,res)
            r+=1
        return res
        
        