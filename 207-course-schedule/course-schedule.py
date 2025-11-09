from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0] * numCourses  # in-degree count for each course
        
        # Build graph + in-degree
        for crs, pre in prerequisites:
            graph[pre].append(crs)     # pre → crs (edge direction)
            indegree[crs] += 1         # crs depends on one more prerequisite

        # ✅ Step 1: Start with all nodes having indegree 0 (no prereqs)
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        taken = 0  # count of courses that can be completed

        # ✅ Step 2: BFS-like traversal
        while queue:
            course = queue.popleft()
            taken += 1  # mark this course as completed

            # Reduce indegree for dependent courses
            for neighbor in graph[course]:
                indegree[neighbor] -= 1
                # If a course now has no prerequisites, add it to queue
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        # ✅ Step 3: If we completed all courses, no cycle exists
        return taken == numCourses
