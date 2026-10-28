
from collections import deque

def search(maze, start, goal, bfs=False):
    stack = deque([start])
    parent = {start: None}

    while stack:
        r, c = stack.popleft() if bfs else stack.pop()
        if (r, c) == goal:
            break

        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            p = (r+dr, c+dc)
            if (0 <= p[0] < len(maze) and 0 <= p[1] < len(maze[0])
                and maze[p[0]][p[1]] != '#' and p not in parent):
                parent[p] = (r, c)
                stack.append(p)

    if goal not in parent:
        return []

    path, p = [], goal
    while p is not None:
        path.append(p)
        p = parent[p]
    return path[::-1]

maze = [
    ['S', '.', '.', '#'],
    ['#', '.', '.', '#'],
    ['#', '.', '.', '.'],
    ['#', '#', '.', 'G']
]
start, goal = (0, 0), (3, 3)

print("Maze:")
for row in maze:
    print(' '.join(row))

for name, bfs in [("DFS", False), ("BFS", True)]:
    path = search(maze, start, goal, bfs)
    print(f"\n{name} Path:", path)
    print(f"{name} Moves:", len(path)-1 if path else -1)


# D:\college\AIML_MOCK\2.py