class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
    
        
        seen = dict()

        for i in range(len(numbers)):
            diff = target-numbers[i]
            if diff in seen:
                return [seen[diff],i+1]
            seen[numbers[i]] = i+1

        # i,j=0,len(numbers)-1

        # while i<j:
        #     # if numbers[j]>target:
        #     #     j-=1
        #     #     continue
        #     # print(j)
        #     if numbers[i]+numbers[j]==target:
        #         return [i+1,j+1]
        #     i+=1
        #     if i==j:
        #         i=0
        #         j-=1
        