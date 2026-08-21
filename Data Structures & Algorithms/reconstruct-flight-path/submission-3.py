class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # tickets.sort()
        # res=[]
        # adj=defaultdict(list)
        # for i in range(len(tickets)):
        #     adj[tickets[i][0]].append(tickets[i][1])
        # res.append("JFK")
        # def dfs(i):
        #     if len(res)==len(tickets)+1:
        #         return True
        #     if i not in adj:
        #         return False
        #     for j in range(len(adj[i])):
        #         res.append(adj[i][j])
        #         destination=adj[i].pop(j)
                
                
        #         if dfs(destination):
        #             return True
        #         res.pop()
        #         adj[i].insert(j,destination)
        #     return False
        # dfs("JFK")
        # return res
        adj=defaultdict(list)
        tickets.sort(reverse=True)
        for i in range(len(tickets)):
            adj[tickets[i][0]].append(tickets[i][1])
        res=[]
        def dfs(i):
            while adj[i]:
                dfs(adj[i].pop())
            res.append(i)
        dfs("JFK")
        return res[::-1]

            


        