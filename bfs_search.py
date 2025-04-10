import sys
from collections import deque

def read_problem(filename):
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]

    nodes = {}           # Stores node coordinates like {1: (4,1)}
    edges = {}           # Stores edges like {1: [(3, 5)]}
    origin = None        # The starting node
    destinations = []    # List of goal nodes

    section = None
    for line in lines:
        if line.startswith("Nodes:"):
            section = "nodes"
        elif line.startswith("Edges:"):
            section = "edges"
        elif line.startswith("Origin:"):
            section = "origin"
        elif line.startswith("Destinations:"):
            section = "destinations"
        else:
            if section == "nodes":
                node_id, coord = line.split(":")
                nodes[int(node_id)] = eval(coord.strip())
            elif section == "edges":
                edge, cost = line.split(":")
                u, v = eval(edge.strip())
                edges.setdefault(u, []).append((v, int(cost.strip())))
            elif section == "origin":
                origin = int(line.strip())
            elif section == "destinations":
                destinations = list(map(int, line.split(";")))

    return nodes, edges, origin, destinations

def reconstruct_path(came_from, goal):
    path = [goal]
    while goal in came_from:
        goal = came_from[goal]
        path.append(goal)
    return path[::-1]

def bfs(origin, destinations, edges):
    queue = deque([origin])
    visited = set()
    came_from = {}
    nodes_generated = 0

    while queue:
        current = queue.popleft()
        nodes_generated += 1
        if current in destinations:
            return current, nodes_generated, reconstruct_path(came_from, current)
        visited.add(current)
        for neighbor, _ in sorted(edges.get(current, [])):  # sorted for consistent node order
            if neighbor not in visited and neighbor not in queue:
                came_from[neighbor] = current
                queue.append(neighbor)

    return None, nodes_generated, []

def main():
    if len(sys.argv) != 2:
        print("Usage: python bfs_search.py <filename>")
        return

    filename = sys.argv[1]
    node_pos, edges, origin, destinations = read_problem(filename)

    goal, count, path = bfs(origin, destinations, edges)

    print(f"{filename} BFS")
    if path:
        print(f"{goal} {count}")
        print(" -> ".join(map(str, path)))
    else:
        print("No path found")

if __name__ == "__main__":
    main()
