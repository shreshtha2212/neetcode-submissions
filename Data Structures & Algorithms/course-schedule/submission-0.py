class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dependencyList=defaultdict(list)
        vis=[0]*numCourses
        pathVis=[0]*numCourses
        def dfs(i):
            vis[i]=1
            pathVis[i]=1
            for j in dependencyList[i]:
                if vis[j]==0:
                    if not dfs(j):
                        return False
                else:
                    if pathVis[j]:
                        return False
            pathVis[i]=0
            return True

        for i in prerequisites:
            dependencyList[i[0]].append(i[1])
        for i in range(numCourses):
            if vis[i]==0:
                if not dfs(i):
                    return False
        return True

        
            
        