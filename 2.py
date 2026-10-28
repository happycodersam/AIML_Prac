
from collections import deque

maze = [
    ['S', '.', '.', '#'],
    ['#', '.', '.', '#'],
    ['#', '.', '.', '.'],
    ['#', '#', '.', 'G']
]
start, goal = (0, 0), (3, 3)
dirs = [(-1,0), (1,0), (0,-1), (0,1)]

def solve(frontier, bfs):
    parent = {start: None}
    while frontier:
        p = frontier.popleft() if bfs else frontier.pop()
        if p == goal:
            break
        for dr, dc in dirs:
            r, c = p[0]+dr, p[1]+dc
            q = (r, c)
            if (0 <= r < len(maze) and 0 <= c < len(maze[0])
                and maze[r][c] != '#' and q not in parent):
                parent[q] = p
                frontier.append(q)

    if goal not in parent:
        return []
    path, p = [], goal
    while p is not None:
        path.append(p)
        p = parent[p]
    return path[::-1]

def bfs():
    return solve(deque([start]), True)

def dfs():
    return solve([start], False)

print("Maze:")
for row in maze:
    print(' '.join(row))

for name, fn in [("BFS", bfs), ("DFS", dfs)]:
    path = fn()
    print(f"\n{name} Path:", path)
    print(f"{name} Moves:", len(path)-1 if path else -1)
