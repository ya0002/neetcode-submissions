class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        while len(stones)>1:
            stones = sorted(stones)
            x,y= stones[-2],stones[-1]
            print(stones)
            if x==y:
                stones=stones[:-2]
            elif x<y:
                stones[-1] = y-x
                stones.remove(x)
            print(stones)
        
        return stones[0] if stones else 0
