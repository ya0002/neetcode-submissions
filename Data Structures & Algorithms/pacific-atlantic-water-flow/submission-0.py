class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        ROWS, COLS= len(heights),len(heights[0])

        pacific= set() ## entire 0th row and 0th col
        atlantic = set() ## entire (ROWS-1)th row and (COL-1)th col

        ## since we are going from ocean to cells, condition is reversed. 
        ## we can reach from low to high or equal
        

        def dfs(set_grp,i,j):
            # print("at",i,j)
            deltas = [[1,0],[-1,0],[0,1],[0,-1]]

            for dr,dc in deltas:
                r,c = i+dr,j+dc
                if ((r,c) not in set_grp and 
                    r in range(ROWS) and c in range(COLS) 
                    and heights[i][j]<=heights[r][c] 
                    ):
                    # print("adding",r,c)
                    set_grp.add((r,c))
                    dfs(set_grp,r,c)
            return
        
        ## pacific
        i=0
        for j in range(COLS):
            if (i,j) not in pacific:
                pacific.add((i,j))
                dfs(pacific,i,j)
        
        j=0
        for i in range(ROWS):
            if (i,j) not in pacific:
                pacific.add((i,j))
                dfs(pacific,i,j)

        ## atlantic
        # print("atlantic")
        i=ROWS-1
        for j in range(COLS):
            if (i,j) not in atlantic:
                atlantic.add((i,j))
                dfs(atlantic,i,j)
        
        j=COLS-1
        for i in range(ROWS):
            if (i,j) not in atlantic:
                atlantic.add((i,j))
                dfs(atlantic,i,j)

        ## intersection
        res = [list(i) for i in pacific.intersection(atlantic)]
        # print(pacific,'\n',atlantic,'\n',res)
        return res
        
        

         