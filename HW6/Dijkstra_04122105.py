from collections import defaultdict 


class Graph(): 

    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [] 
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
        
    def addEdge(self,u,v,w): 
        self.graph.append([w,u,v]) 

        
        
    def Dijkstra(self, s): 
        dis = [99999] * self.V
        seen = [False] * self.V
        dis[s] = 0
        while seen != [True] * self.V:
            for i in range(self.V):
                if g.graph[s][i] != 0 and dis[s] + g.graph[s][i] < dis[i]:
                    dis[i] = dis[s] + g.graph[s][i]
            k = 99999               
            for j in range(self.V):
                if seen[j] == False and dis[j] < k :  #小於原本的數就更新
                    k = dis[j]
                    s = j         
            seen[s] = True
            
            dictionary = {} 
            if seen == [True] * self.V:
                for i in range(self.V):
                    dictionary[str(i)] = dis [i]
                return dictionary    
            

        
        
    def Kruskal(self):
        pass
