from collections import defaultdict
from copy import deepcopy

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        s1freq= defaultdict(int)
        for c in s1:
            s1freq[c] +=1
        
        window_len = len(s1)

        for l in range(len(s2)-(window_len-1)):
            r = l+window_len
            
            #extract possible sequence
            s2seq = s2[l:r]

            s1freq_copy = deepcopy(s1freq)
            for c in s2seq:
                if c not in s1freq_copy:
                    break
                # print(s1freq_copy,s2seq)
                s1freq_copy[c]-=1

            if all(v==0 for v in s1freq_copy.values()):
                return True
        
        return False
            
            

            