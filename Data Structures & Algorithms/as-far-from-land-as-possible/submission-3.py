from collections import deque

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        ROWS,COLS=len(grid),len(grid[0])
        
        dists = set()
        d=0
        deltas = [[1,0],[-1,0],[0,1],[0,-1]]
        visited=set()

        q= deque()
        ct_1s,ct_0s=0,0

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]:
                    q.append([i,j,0])
                    visited.add((i,j))
                    ct_1s+=1
                else:
                    # q.append([i,j])
                    ct_0s+=1
        
        ## means no land or water
        if not ct_0s or not ct_1s:
            return -1

        
        ## Run multi-source BFS
        while q:
            R,C,D = q.popleft()
            for dr,dc in deltas:
                r,c=R+dr,C+dc

                if (
                    r in range(ROWS) and c in range(COLS)
                    and (r,c) not in visited and grid[r][c]==0
                    ):
                    curr_d = abs(R-r)+abs(C-c)+D
                    d = max(d, curr_d)
                    visited.add((r,c))
                    q.append([r,c,curr_d]) ## carry the current cells distance from land with it


        return d
