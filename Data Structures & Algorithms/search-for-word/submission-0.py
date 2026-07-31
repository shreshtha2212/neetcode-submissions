class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows=len(board)
        cols=len(board[0])
        def check(r,c,i,vis):
            if len(word)==i:
                return True
            if r==rows or c==cols or r<0 or c<0 or vis[r][c]==True or board[r][c]!=word[i]:
                return
           
           
            
            vis[r][c]=True

            
            j=check(r+1,c,i+1,vis)
                    
            k=check(r-1,c,i+1,vis)
                   
            l=check(r,c-1,i+1,vis)
                    
            m=check(r,c+1,i+1,vis)
            vis[r][c]=False
            return j or k or l or m
        vis=[[False]*cols for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                if check(r,c,0,vis):
                    return True
        return False
            
            
            
            
        