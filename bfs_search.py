import sys
from collections import deque
from graph import Graph

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
    """Reconstructs the path from origin to goal."""
    path = [goal]
    while goal in came_from:
        goal = came_from[goal]
        path.append(goal)
    return path[::-1]

def bfs(origin, destinations, edges):
    """
    Breadth-First Search implementation.
    - Expands nodes in ascending order when equal
    - Maintains chronological order for equal priority nodes
    - Tracks number of nodes generated
    """
    queue = deque([(origin, [origin])])  # Store node and its path
    visited = set()
    nodes_generated = 0
    
    while queue:
        current, path = queue.popleft()
        nodes_generated += 1
        
        if current in destinations:
            return current, nodes_generated, path
            
        # Get all neighbors and sort them in ascending order
        neighbors = sorted(edges.get(current, []), key=lambda x: x[0])
        
        for neighbor, _ in neighbors:
            if neighbor not in visited and neighbor not in [n for n, _ in queue]:
                visited.add(neighbor)
                new_path = path + [neighbor]
                queue.append((neighbor, new_path))
                
    return None, nodes_generated, []

def main():
    if len(sys.argv) != 2:
        print("Usage: python bfs_search.py <filename>")
        return

    filename = sys.argv[1]
    node_pos, edges, origin, destinations = read_problem(filename)

    # Create graph instance
    graph = Graph(node_pos, edges)
    
    # Run BFS
    goal, count, path = bfs(origin, destinations, edges)

    # Output in required format
    print(f"{filename} BFS")
    if path:
        print(f"{goal} {count}")
        print(" -> ".join(map(str, path)))
    else:
        print("No path found")

if __name__ == "__main__":
    main()
