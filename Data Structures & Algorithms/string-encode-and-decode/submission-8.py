class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs)==0:
            return "[SEP]"

        for i in range(len(strs)):
            if strs[i]=="":
                strs[i]= "[EMP]"
                
        return '[SEP]'.join(strs)

    def decode(self, s: str) -> List[str]:
        if s=="[SEP]":
            return []

        strs = s.split('[SEP]')

        for i in range(len(strs)):
            if strs[i]=="[EMP]":
                strs[i]= ""
        return strs
