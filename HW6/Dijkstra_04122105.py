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
            
##################
        
    def find(self, parent, i): 
        if parent[i] == i: 
            return i 
        return self.find(parent, parent[i]) 
  
    def union(self, parent, rank, x, y): 
        xroot = self.find(parent, x) 
        yroot = self.find(parent, y) 

        if rank[xroot] < rank[yroot]: 
            parent[xroot] = yroot 
        elif rank[xroot] > rank[yroot]: 
            parent[yroot] = xroot 

        else : 
            parent[yroot] = xroot 
            rank[xroot] += 1
  

    def Kruskal(self): 
  
        result =[] 
  
        i = 0 
        e = 0 
        self.graph =  sorted(self.graph,key=lambda item: item[2]) 
        parent = [] ; rank = [] 

        for node in range(self.V): 
            parent.append(node) 
            rank.append(0) 
      
        while e < self.V -1 : 
 
            u,v,w =  self.graph[i] 
            i = i + 1
            x = self.find(parent, u) 
            y = self.find(parent ,v) 
  
         
            if x != y: 
                e = e + 1     
                result.append([u,v,w]) 
                self.union(parent, rank, x, y)             


        for u,v,weight  in result: 
            print ("%d -- %d == %d" % (u,v,weight)) 


#程式碼有參考
