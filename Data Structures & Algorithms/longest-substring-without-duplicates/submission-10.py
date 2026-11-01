class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        seen = set()
        res=0

        l=0

        for r in range(len(s)):
            
            c=s[r]

            while c in seen:
                seen.remove(s[l])
                l+=1
                
                    
            
            seen.add(c)
            res=max(r-l+1,res)
         
        return res
        
        