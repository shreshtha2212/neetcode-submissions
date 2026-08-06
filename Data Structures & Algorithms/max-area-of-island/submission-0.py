class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        vis=set()
        def dfs(i,j):
            if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or (i,j) in vis or grid[i][j]==0:
                return 0
            vis.add((i,j))
            ar=1
            ar+=dfs(i+1,j)
            ar+=dfs(i,j+1)
            ar+=dfs(i-1,j)
            ar+=dfs(i,j-1)
            return ar





        maxAr=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                

                if grid[i][j]==1 and (i,j) not in vis:
                    
                    ar=dfs(i,j)
                    if ar>maxAr:
                        maxAr=max(maxAr,ar)
        return maxAr

        