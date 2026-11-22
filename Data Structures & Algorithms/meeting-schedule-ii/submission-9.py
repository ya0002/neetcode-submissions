"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
from collections import deque

import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        if not intervals:
            return 0

        intervals.sort(key=lambda x:x.start)

        # print([vars(i) for i in intervals])

        res=1
        cur = intervals[0]
        ends = []
        heapq.heappush(ends,cur.end)

        for i in range(1,len(intervals)):
            
            ## if another meeting ended
            if intervals[i].start>=ends[0]:
                heapq.heappop(ends)
                # cur = intervals[i]
            # ## else if there is an overlap with cur
            # elif cur.end>intervals[i].start:
            #     cur.end = max(cur.end, intervals[i].end)
            #     res +=1
            # else:
            #     cur = intervals[i]

            heapq.heappush(ends,intervals[i].end)


        return len(ends)