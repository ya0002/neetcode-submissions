class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        seen = set()
        res=0

        l=0

        for r in range(len(s)):
            
            c=s[r]

            while c in seen:
                ## remove till c is removed, because the new sequence can start only after the position of the duplicate charater(for casba -> ca, sba )
                seen.remove(s[l])
                l+=1  
                    
            seen.add(c)
            res=max(r-l+1,res)
         
        return res
        
        