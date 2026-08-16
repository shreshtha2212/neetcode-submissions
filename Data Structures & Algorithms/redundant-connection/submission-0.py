class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        l=defaultdict(int)
        def findParent(i):
            if i==l[i]:
                return i
            l[i]=findParent(l[i])
            return l[i]
        for i in range(1,len(edges)+1):
            l[i]=i
        for i in range(len(edges)):
            e1=findParent(edges[i][0])
            e2=findParent(edges[i][1])
            if e1==e2:
                return edges[i]
            else:
                l[e1]=findParent(e2)
        return {}


        
