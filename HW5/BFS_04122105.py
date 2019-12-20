from collections import defaultdict 


class Graph:

    def __init__(self): 
        self.graph = defaultdict(list) 

    def addEdge(self,u,v): 
        self.graph[u].append(v) 

    def BFS(self, s): 
        queue = []
        arr = []
        queue.append(s)
        while queue: 
            vertex = queue.pop(0)
            for w in self.graph[vertex]:
                if w not in arr and w not in queue:
                    queue.append(w)         
            if vertex not in arr:
                arr.append(vertex)   

        return arr

  

    def DFS(self, s):
        stack = []
        arr = []
        stack.append(s)
        while stack:  
            vertex = stack.pop(-1)
            for w in self.graph[vertex]:
                if w not in arr and w not in stack:
                    stack.append(w)         
            if vertex not in arr:
                arr.append(vertex)   

        return arr
