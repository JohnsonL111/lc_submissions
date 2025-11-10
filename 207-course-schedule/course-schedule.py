from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Step 1: Build the adjacency list and in-degree array
        graph = defaultdict(list)         # key: course, value: list of next courses
        indegree = [0] * numCourses       # indegree[i] = number of prerequisites for course i

        # Fill in graph and indegree counts
        for pair in prerequisites:
            course = pair[0]
            prereq = pair[1]

            # prereq -> course (you must take prereq before course)
            graph[prereq].append(course)
            indegree[course] += 1

        # Step 2: Initialize the queue with all courses that have no prerequisites (in-degree = 0)
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        # Step 3: Process the queue in BFS order
        courses_taken = 0  # counts how many courses we can finish

        while len(queue) > 0:
            # Remove a course from the queue
            current = queue.popleft()
            courses_taken += 1

            # For each course that depends on the current one
            for neighbor in graph[current]:
                # One prerequisite has now been satisfied
                indegree[neighbor] -= 1

                # If that course now has no prerequisites left, add it to the queue
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        # Step 4: Check if we were able to take all courses
        # If we processed all nodes, there was no cycle
        if courses_taken == numCourses:
            return True
        else:
            return False
