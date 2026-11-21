from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        ROWS,COLS=len(grid),len(grid[0])

        q= deque()
        # visited = set()
        deltas=[[1,0],[-1,0],[0,1],[0,-1]]
        time=-1## we start counting at 0,  time += 1 should be 0 in the beginning
        num_1s = 0

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]==2:
                    q.append([i,j])
                elif grid[i][j]==1:
                    num_1s += 1
        
        if not q and not num_1s:
            return 0

        flipped = 0
        while q:
            
            ## everytime q i s completly emptied, its 1 minute
            q_pops=[]
            while q:
                q_pops.append(q.popleft())
            time += 1
            
            ## add the valid neighbors for processing
            for R,C in q_pops:
                # visited.add((R,C))
                for dr,dc in deltas:
                    r,c=R+dr,C+dc
                    if (
                        r in range(ROWS) and c in range(COLS)
                        # and (r,c) not in visited 
                        and grid[r][c]==1
                    ):
                        grid[r][c]=2
                        flipped+=1
                        q.append([r,c])
        
                    
        if flipped!=num_1s:
            return -1

        return time
