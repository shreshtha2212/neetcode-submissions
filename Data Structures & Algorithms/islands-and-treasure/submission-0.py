class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q=deque()
        dirn=[(1,0),(-1,0),(0,-1),(0,1)]
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]==0:
                    q.append((r,c))
        while q:
            r,c=q.popleft()
            for dr,dc in dirn:
                nr=r+dr
                nc=c+dc
                if nr<0 or nc<0 or nr>=len(grid) or nc>=len(grid[0]):
                    continue
                if grid[nr][nc]!=2147483647:
                    continue
                
                grid[nr][nc]=grid[r][c]+1
                q.append((nr,nc))


        