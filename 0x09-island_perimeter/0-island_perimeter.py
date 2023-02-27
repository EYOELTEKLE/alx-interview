#!/usr/bin/python3
"""
dfs solution
"""


def island_perimeter(grid):
    visited = set()
    count = 0

    def dfs(i, j):

        b1 = 0 <= i and i < len(grid)
        b2 = 0 <= j and j < len(grid[0])
        perimeter = 0

        if not b1 or not b2:
            return 1
        if str(i) + ',' + str(j) in visited:
            return 0
        if grid[i][j] == 0:
            return 1
        visited.add(str(i) + ',' + str(j))
        perimeter += dfs(i+1, j)
        perimeter += dfs(i-1, j)
        perimeter += dfs(i, j+1)
        perimeter += dfs(i, j-1)
        return perimeter
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            ans = dfs(i, j)
            if count == 0 or ans > count:
                count = ans
    return count
