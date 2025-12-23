class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # convert edges into adjacency list
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = set()
        cc = 0

        def bfs(node: int):
            queue = deque([node])

            while queue:
                curr = queue.popleft() 
                for neighbor in adj[curr]:
                    if neighbor not in visited:
                        queue.append(neighbor)
                        visited.add(neighbor)
        
        # call bfs for each vertex
        for i in range(0, n):
            if i not in visited:
                cc += 1
                bfs(i)

        return cc



        