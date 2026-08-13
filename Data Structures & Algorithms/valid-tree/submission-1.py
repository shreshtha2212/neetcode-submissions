class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)!=n-1:
            return False
        dependencyList=defaultdict(list)
        for i in edges:
            dependencyList[i[0]].append(i[1])
            dependencyList[i[1]].append(i[0])
        vis=[0]*n
        def dfs(i,parent):
            vis[i]=1
            for j in dependencyList[i]:
                if not vis[j]:
                    if dfs(j,i):
                        return True
                else:
                    if j!=parent:
                        return True
            return False
        if dfs(0,-1):
            return False
        if sum(vis)!=n:
            return False
        return True





        