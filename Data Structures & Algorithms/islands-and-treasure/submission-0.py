from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        deltas = [[1,0],[-1,0],[0,1],[0,-1]]
        ROWS,COLS = len(grid),len(grid[0])

        q=deque()
        visited = set()

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]==0:
                    q.append([i,j])
        

        while q:

            R,C = q.popleft()
            cell_val = grid[R][C]

            for dr,dc in deltas:
                r,c=R+dr,C+dc
                if (
                    r in range(ROWS) and c in range(COLS)
                    and grid[r][c]>0
                    and (r,c) not in visited
                ):
                    grid[r][c] = min(cell_val+1,grid[r][c])
                    q.append([r,c])
                    visited.add((r,c))






        