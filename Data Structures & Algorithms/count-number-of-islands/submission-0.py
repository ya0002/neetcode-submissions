class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0
        
        visited= set()
        row,cols= len(grid),len(grid[0])
        cnt=0

        def bfs(i,j):
            q=deque()
            q.append((i,j))
            visited.add((i,j))

            deltas =[(-1,0),(1,0),(0,1),(0,-1)]

            while q:
                vis_r,vis_c= q.pop()
                
                for dr,dc in deltas:    
                    r,c= vis_r+dr, vis_c+dc
                    if r in range(row) and c in range(cols) and (r,c) not in visited and grid[r][c]=="1":
                        visited.add((r,c))
                        q.append((r,c))

        for i in range(row):
            for j in range(cols):
                if grid[i][j]=="1" and (i,j) not in visited:
                    bfs(i,j)
                    cnt+=1
        return cnt