class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific=set()
        atlantic=set()
        dirn=[(-1,0),(0,-1),(1,0),(0,1)]
        def dfs(i,j,vis):
            
            vis.add((i,j))
            for dr,dc in dirn:
                nr,nc=i+dr, j+dc
                if nr>=len(heights) or nc>=len(heights[0]) or nr<0 or nc<0 or (nr,nc) in vis or heights[nr][nc]<heights[i][j]:
                    continue
                
                dfs(nr,nc,vis)
        for i in range(len(heights)):
            dfs(i,0,pacific)
            dfs(i,len(heights[0])-1,atlantic)
        for j in range(len(heights[0])):
            dfs(0,j,pacific)
            dfs(len(heights)-1,j,atlantic)
        return [[r, c] for r in range(len(heights))
                        for c in range(len(heights[0]))
                        if (r, c) in pacific and (r, c) in atlantic]

        