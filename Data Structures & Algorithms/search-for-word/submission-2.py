class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        self.word_exists = False
        self.visited=set()

        def dfs(i,j,cur,w_i):
            if cur==word:
                self.word_exists = True
            if (
                self.word_exists or (i,j) in self.visited 
                or i>len(board)-1 or i<0 or j>len(board[0])-1 or j<0
                or board[i][j]!=word[w_i]
                ):
                return
            
            c = board[i][j]
            print("chr",c,(i,j),"cur",cur,word[w_i])
            self.visited.add((i,j))
            dfs(i-1,j,cur+c,w_i+1)
            dfs(i+1,j,cur+c,w_i+1)
            dfs(i,j-1,cur+c,w_i+1)
            dfs(i,j+1,cur+c,w_i+1)
            self.visited.remove((i,j))
           
        for i in range(len(board)):
            for j in range(len(board[0])):
                print('NEW')
                dfs(i,j,"",0)
                if self.word_exists:
                    return True

        return self.word_exists