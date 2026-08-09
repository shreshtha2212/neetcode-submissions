class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q=deque()
        t=0
        dirn=[(1,0),(0,1),(-1,0),(0,-1)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    q.append((i,j))
        while q:
            flag=0
            
            for _ in range(len(q)):
                r,c=q.popleft()
                
                for dr, dc in dirn:
                    nr, nc=r+dr, c+dc
                    if nr<0 or nc<0 or nr>=len(grid) or nc>=len(grid[0]):
                        continue
                    if grid[nr][nc]==0 or grid[nr][nc]==2:
                        continue
                    grid[nr][nc]=2
                    flag=1
                
                    q.append((nr,nc))
            if flag==1:
                t+=1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    return -1
        return t



        