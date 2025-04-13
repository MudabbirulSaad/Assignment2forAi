import sys
from methods.bfs_search import bfs
from methods.dfs_search import dfs
from methods.gbfs_search import gbfs
from methods.astar_search import astar
from methods.iddfs_search import iddfs
from methods.bdwa_search import bdwa
from input_parser import build_data
from graph import Graph

def get_scenario_description(filename):
    """Extract scenario description from a file if it exists (lines starting with #)"""
    scenario = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                if line.strip().startswith('#'):
                    scenario.append(line.strip()[1:].strip())
                elif line.strip().startswith('Nodes:'):
                    break
    except:
        return ""
    
    return "\n".join(scenario) if scenario else ""

def extract_node_names(filename):
    """Extract node names from comments in the node definitions"""
    node_names = {}
    try:
        in_nodes_section = False
        with open(filename, 'r') as f:
            for line in f:
                line = line.strip()
                if line.startswith('Nodes:'):
                    in_nodes_section = True
                    continue
                elif line.startswith('Edges:'):
                    in_nodes_section = False
                    break
                
                if in_nodes_section and ':' in line and '#' in line:
                    # Extract node ID and name from lines like "1: (0,0)    # Downtown Central Station"
                    parts = line.split(':', 1)
                    node_id = parts[0].strip()
                    comment_parts = parts[1].split('#', 1)
                    if len(comment_parts) > 1:
                        node_name = comment_parts[1].strip()
                        node_names[int(node_id)] = node_name
    except Exception as e:
        print(f"# Note: Couldn't extract node names: {str(e)}")
    
    return node_names

def main():
    if len(sys.argv) != 3:
        print("Usage: python search.py <filename> <method>")
        print("Available methods: BFS, DFS, GBFS, AS, CUS1, CUS2")
        return

    filename = sys.argv[1]
    method = sys.argv[2].upper()

    # Read the problem using the dedicated input parser
    node_pos, edges, origin, destinations = build_data(filename)

    # Create graph instance
    graph = Graph(node_pos, edges)
    
    # Get scenario description if it exists
    scenario = get_scenario_description(filename)
    if scenario:
        print(f"# {scenario}")
        print("#")
    
    # Extract node names for human-readable output
    node_names = extract_node_names(filename)
    
    # Select and run the appropriate search method
    if method == "BFS":
        goal, count, path = bfs(origin, destinations, edges)
    elif method == "DFS":
        goal, count, path = dfs(origin, destinations, edges)
    elif method == "GBFS":
        goal, count, path = gbfs(origin, destinations, edges, node_pos)
    elif method == "AS":
        goal, count, path = astar(origin, destinations, edges, node_pos)
    elif method == "CUS1":
        goal, count, path = iddfs(origin, destinations, edges)
    elif method == "CUS2":
        goal, count, path = bdwa(origin, destinations, edges, node_pos)
    else:
        print(f"Error: Unknown method '{method}'")
        print("Available methods: BFS, DFS, GBFS, AS, CUS1, CUS2")
        return

    # Output in required format (must follow assignment requirements)
    print(f"{filename} {method}")
    if path:
        # First line is the standard output required by the assignment
        print(f"{goal} {count}")
        
        # Second line is the standard path required by the assignment
        print(" -> ".join(map(str, path)))
        
        # Add human-readable path as a comment
        print("#")
        print("# Human-readable path with location names:")
        
        # Print each node on its own line with comment prefix
        for i, node_id in enumerate(path):
            node_desc = f"{node_id}"
            if node_id in node_names:
                node_desc += f" ({node_names[node_id]})"
                
            if i == 0:
                print(f"# Start: {node_desc}")
            elif i == len(path) - 1:
                print(f"# Goal:  {node_desc}")
            else:
                print(f"# Via:   {node_desc}")
    else:
        print("No path found")

if __name__ == "__main__":
    main() 