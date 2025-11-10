from collections import defaultdict, deque

class Solution:
    def findOrder(self, numNodes: int, prerequisites: List[List[int]]) -> List[int]:
        # 1️⃣ Build adjacency list and indegree array
        graph = defaultdict(list)
        indegree = [0] * numNodes

        for dest, src in prerequisites:   # src → dest
            graph[src].append(dest)
            indegree[dest] += 1

        # 2️⃣ Initialize queue with all nodes that have indegree 0
        queue = deque()
        for i in range(numNodes):
            if indegree[i] == 0:
                queue.append(i)

        # ✅ (Added for Course Schedule II)
        order = []                         # <-- NEW: store the topological order

        # 3️⃣ BFS (Kahn’s Algorithm)
        while queue:
            node = queue.popleft()
            # ✅ (Added for Course Schedule II)
            order.append(node)              # <-- NEW: record the node order as we process

            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        # 4️⃣ Return the order if valid, otherwise []
        # ✅ (Modified for Course Schedule II)
        if len(order) == numNodes:          # check all nodes processed
            return order                    # <-- NEW: return the order instead of True/False
        else:
            return []                       # cycle detected → return empty list
