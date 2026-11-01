class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        if len(s)<=k:
            return len(s)
        
        freq=dict()
        
        res = 0
        l=0

        for r,c in enumerate(s):
            freq[c] = freq.get(c,0) + 1
            maxf = max(freq.values())

            seq_len = r-l+1

            if seq_len-maxf<=k: ## figure out if number of replaceble chars are k
                res = max(seq_len, res)
            else:
                freq[s[l]] -=1
                l+=1 # move the window
        return res




        