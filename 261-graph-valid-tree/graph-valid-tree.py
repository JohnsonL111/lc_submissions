class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # no self loops or repeated edges allowed in trees
        # for graph G to be a tree:
        #(1), G is fully connected. For every pair of nodes in G there is a path between them.
        #(2), G has no cycles. Exactly 1 path between each pair of nodes in G
        
        # if dfs visits a node we've already seen then there is a cycle
        # fast check if valid tree: # edges = n-1
        if len(edges) != n - 1:
            return False

        # convert edges into adjacency list (easier to run dfs)
        # run dfs and check if node appears twice in visit. If yes then not valid tree.

        adj = defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        # both visited set and adj list are in the closure
        visited: Set[int] = set()
        # need parent in dfs of undirected graph to check against trivial a->b, b->a cycle
        def dfs(node: int, parent: int) -> bool:
            visited.add(node)
            
            for neighbor in adj[node]:
                if neighbor == parent: # dont count the trivial cycle
                    continue
                if neighbor in visited: # cycle
                    return False
                if not dfs(neighbor, node):
                    return False

            return True

        # cycle check
        if not dfs(0,-1):
            return False

        # final connectivity check 
        return True if len(visited) == n else False





        

        




        