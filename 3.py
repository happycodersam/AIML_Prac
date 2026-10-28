
import heapq

maze = [
    [0, 0, 0, 1, 0],
    [1, 0, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 0, 1],
    [0, 0, 0, 0, 0]
]
start, goal = (0, 0), (4, 4)

def search(astar=False):
    h = lambda p: abs(p[0]-goal[0]) + abs(p[1]-goal[1])
    heap = [(h(start), 0, start, [start])]
    visited = set()

    while heap:
        _, cost, (r, c), path = heapq.heappop(heap)
        if (r, c) == goal:
            return path
        if (r, c) in visited:
            continue
        visited.add((r, c))

        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            p = (r+dr, c+dc)
            if (0 <= p[0] < len(maze) and 0 <= p[1] < len(maze[0])
                and maze[p[0]][p[1]] == 0 and p not in visited):
                g = cost + 1
                heapq.heappush(heap, (g+h(p) if astar else h(p),
                                      g, p, path+[p]))
    return []

for name, astar in [("GBFS", False), ("A*", True)]:
    path = search(astar)
    result = [['#' if x else '.' for x in row] for row in maze]
    for r, c in path:
        result[r][c] = 'P'
    result[start[0]][start[1]], result[goal[0]][goal[1]] = 'S', 'G'
    print(f"\n{name} Path ({len(path)-1} moves):")
    for row in result:
        print(' '.join(row))
