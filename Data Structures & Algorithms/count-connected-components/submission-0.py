class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dependencyList=defaultdict(list)
        vis=[0]*n
        c=0
        for i in edges:
            dependencyList[i[0]].append(i[1])
            dependencyList[i[1]].append(i[0])
        def dfs(i):
            vis[i]=1
            for j in dependencyList[i]:
                if not vis[j]:
                    dfs(j)
        for i in range(n):
            if not vis[i]:
                dfs(i)
                c+=1
        return c

        
        