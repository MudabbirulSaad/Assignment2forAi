import sys
from bfs_search import bfs
from dfs_search import dfs
from gbfs_search import gbfs
from input_parser import build_data
from graph import Graph

def main():
    if len(sys.argv) != 3:
        print("Usage: python search.py <filename> <method>")
        print("Available methods: BFS, DFS, GBFS")
        return

    filename = sys.argv[1]
    method = sys.argv[2].upper()

    # Read the problem using the dedicated input parser
    node_pos, edges, origin, destinations = build_data(filename)

    # Create graph instance
    graph = Graph(node_pos, edges)
    
    # Select and run the appropriate search method
    if method == "BFS":
        goal, count, path = bfs(origin, destinations, edges)
    elif method == "DFS":
        goal, count, path = dfs(origin, destinations, edges)
    elif method == "GBFS":
        goal, count, path = gbfs(origin, destinations, edges, node_pos)
    else:
        print(f"Error: Unknown method '{method}'")
        print("Available methods: BFS, DFS, GBFS")
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