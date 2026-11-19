import heapq
from collections import deque,Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        tcnt = Counter(tasks)
        
        maxHeap=[]
        for i in tcnt.values():
            maxHeap.append(-i)
        heapq.heapify(maxHeap)

        q = deque()
        time=0

        while q or maxHeap:

            time+=1

            if maxHeap:
                freq= heapq.heappop(maxHeap)
                freq +=1
                ## if freq!=0
                if freq:
                    q.append([freq,time+n])

            if q and q[0][1]==time:
                f,_ = q.popleft()
                heapq.heappush(maxHeap,f)

        return time
        