import sys
from bfs_search import bfs, read_problem as bfs_read
from dfs_search import dfs
from graph import Graph

def main():
    if len(sys.argv) != 3:
        print("Usage: python search.py <filename> <method>")
        print("Available methods: BFS, DFS")
        return

    filename = sys.argv[1]
    method = sys.argv[2].upper()

    # Read the problem
    node_pos, edges, origin, destinations = bfs_read(filename)  # We can use either read_problem function as they're identical

    # Create graph instance
    graph = Graph(node_pos, edges)
    
    # Select and run the appropriate search method
    if method == "BFS":
        goal, count, path = bfs(origin, destinations, edges)
    elif method == "DFS":
        goal, count, path = dfs(origin, destinations, edges)
    else:
        print(f"Error: Unknown method '{method}'")
        print("Available methods: BFS, DFS")
        return

    # Output in required format
    print(f"{filename} {method}")
    if path:
        print(f"{goal} {count}")
        print(" -> ".join(map(str, path)))
    else:
        print("No path found")

if __name__ == "__main__":
    main() 