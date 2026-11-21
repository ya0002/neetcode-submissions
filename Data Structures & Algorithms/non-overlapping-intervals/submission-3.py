class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort()
        print(intervals)
        
        # res = []
        
        merges = 0
        cur = intervals[0]

        for i in range(1,len(intervals)):

            if cur[1]>intervals[i][0]:
                cur[1] = min(intervals[i][1],cur[1]) ##keep the one that ends first,ie, remove the one that ends later because that way we minimize the chances of the longer one overlapping
                merges += 1
            else:
                # res.append(cur)
                cur=intervals[i]

        # res.append(cur)
        # print(res)
        

        return merges
        