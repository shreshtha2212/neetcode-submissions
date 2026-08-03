class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        board = [["."] * n for _ in range(n)]
        leftRow=[0]*n
        upperDiagonal=[0]*(2*n-1)
        lowerDiagonal=[0]*(2*n-1)
        ans=[]
        def solve(col,board,l,ud,ld):
            if col==n:
                ans.append(["".join(row) for row in board])
                return
            for i in range(n):
                if l[i]==0 and ud[n-1+col-i]==0 and ld[i+col]==0:
                    board[i][col]='Q'
                    l[i]=1
                    ld[i+col]=1
                    ud[n-1+col-i]=1
                    solve(col+1,board,l,ud,ld)
                    board[i][col]='.'
                    l[i]=0
                    ld[i+col]=0
                    ud[n-1+col-i]=0

        solve(0,board,leftRow,upperDiagonal, lowerDiagonal)
        return ans

        