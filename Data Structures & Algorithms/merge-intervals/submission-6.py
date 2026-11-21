class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        if len(intervals)==1:
            return intervals
        if not intervals:
            return []

        intervals = sorted(intervals) ## sort 

        res = []
        newInterval = intervals[0]
        

        for i in range(1,len(intervals)):
            
            if newInterval[1]>=intervals[i][0]:
                newInterval = [min(intervals[i][0],newInterval[0]),max(intervals[i][1],newInterval[1])]
            else:
                res.append(newInterval)
                newInterval = intervals[i] ## everyt interval has potential for merging,check first
                
                ##=======WRONG==================
                # if new_merge or not res:
                #     res.append(newInterval)
                #     new_merge = False
                
                # res.append(intervals[i])
                ##=======WRONG==================
        
        #since the last element is not merged in the loop
        res.append(newInterval)

        return res