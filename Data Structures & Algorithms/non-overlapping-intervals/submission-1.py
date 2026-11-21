class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort()
        print(intervals)
        
        res = []
        
        merges = 0
        cur = intervals[0]

        for i in range(1,len(intervals)):

            if cur[1]>intervals[i][0]:
                cur[1] = min(intervals[i][1],cur[1])
                merges += 1
            else:
                res.append(cur)
                cur=intervals[i]

        res.append(cur)
        print(res)
        

        return merges
        