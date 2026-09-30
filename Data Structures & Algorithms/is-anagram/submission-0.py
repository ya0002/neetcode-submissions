class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s)!=len(t):
            return False

        cnts =dict()
        for i,j in zip(s,t):
            cnts[i] = cnts.get(i,0)+1
            cnts[j] = cnts.get(j,0)-1
        
        for i in cnts.values():
            if i!=0:
                return False
        
        return True
        