class Solution:
    def solve(self, board: List[List[str]]) -> None:
        vis = [[0] * len(board[0]) for _ in range(len(board))]
        dirn=[(0,1),(1,0),(0,-1),(-1,0)]
        def dfs(i,j):
            if i<0 or j<0 or i>=len(board) or j>=len(board[0]) or board[i][j]=='X' or vis[i][j]==1:
                return
            vis[i][j]=1
            for dr,dc in dirn:
                nr, nc=i+dr, j+dc
                dfs(nr,nc)
            
        for i in range(len(board[0])):
           
            dfs(0,i)
            dfs(len(board)-1,i)
        for i in range(len(board)):
            
            dfs(i,0)
            dfs(i,len(board[0])-1)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]=='O' and vis[i][j]==0:
                    board[i][j]='X'
        
        
        

            
        