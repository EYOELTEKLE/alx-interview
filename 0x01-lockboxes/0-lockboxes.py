#!/usr/bin/python3
"""
Solution to lockboxes problem
"""


def canUnlockAll(boxes):
    """
    Determines whether a series of locked boxes can be opened
    based on keys that can be attained.
    Solution to the lockboxes problem
    """
    seen = [False for i in range(len(boxes))]

    def getGraph(graph={}):
        """
        adjacencyList graph
        """
        for i in range(len(boxes)):
            for j in range(len(boxes[i])):
                if i not in graph:
                    graph[i] = []
                graph[i].append(boxes[i][j])
        return graph

    graph = getGraph()

    def dfs(src):
        """
        DFS function
        """
        stack = [src]

        while len(stack) > 0:
            current = stack.pop()
            if current in visited:
                continue
            visited.add(current)

            if int(current) != int(src):
                seen[int(current)] = True
            if current in graph:
                for item in graph[current]:
                    stack.append(item)

    visited = set()
    seen[0] = True
    for item in graph:
        dfs(item)
    for val in seen:
        if val is False:
            return False
    return True
