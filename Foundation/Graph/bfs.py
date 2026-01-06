from collections import deque

class Solution:
    def bfs(self,graph,start):
        visited=set()
        queue=deque()
        
        queue.append(start)
        visited.add(start)
        
        while queue:
            node=queue.popleft()
            print(node,end="")
            
            for neighbour in graph[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)

graph = {
  0: [1],
  1: [0, 2],
  2: [1, 3],
  3: [2]
}
s=Solution()
s.bfs(graph,0)