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
            heapq.heappush(ends,intervals[i].end)
            ## overlap
            if intervals[i].start>=ends[0]:
                # print(f"cur {vars(intervals[i])}")
                heapq.heappop(ends)
                cur = intervals[i]
            elif cur.end>intervals[i].start:
                # print(f'MERGING {vars(cur)} and {vars(intervals[i])}')
                cur.end = max(cur.end, intervals[i].end)
                res +=1
            else:
                # print(f"cur {intervals[i]}")
                cur = intervals[i]

        return res