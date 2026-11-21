class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        if not intervals:
            return [newInterval]

        res = []
        new_merged = False

        for idx,itv in enumerate(intervals):
            
            if itv[1]<newInterval[0]:
                ## add all intervals smaller than new interval
                res.append(itv)
            elif itv[1]>=newInterval[0] and itv[0]<=newInterval[1]:
                ## merge all overlaps
                newInterval = [min(itv[0],newInterval[0]),max(itv[1],newInterval[1])]
            else:
                ## add all remaining intervals after merging overlaps
                ## OR newInterval in the beginning if its smaller than the 0th interval: (itv[0]>newInterval[1] and not res)
                if not new_merged:
                    res.append(newInterval)
                    new_merged = True
                res.append(itv)
           
            
        if not new_merged:
            ## if newInterval is the greatest interval
            res.append(newInterval)
            

        return res
        