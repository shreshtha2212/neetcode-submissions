class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        stack=[]
        vis=[0]*numCourses
        pathVis=[0]*numCourses
        dependencyList=defaultdict(list)
        for i in prerequisites:
            dependencyList[i[0]].append(i[1])
        def dfs(i):
            vis[i]=1
            pathVis[i]=1
            for j in dependencyList[i]:
                if vis[j]==0:
                    if dfs(j)==[]:
                        return [] 
                else:
                    if pathVis[j]==1:
                        return []
                    
            pathVis[i]=0
            stack.append(i)

        
        for i in range(numCourses):
            if not vis[i]:
                if dfs(i)==[]:
                    return []
        return stack



        