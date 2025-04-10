import sys
from input_parser import build_data

# -----------------------------------------------------------------------------
# reconstruct_path:
# -----------------------------------------------------------------------------
def reconstruct_path(came_from, goal):
    """
    Reconstructs the path from the origin to the goal using the came_from dictionary.
    
    Args:
        came_from: Dictionary mapping each node to its predecessor in the search.
        goal: The goal node where the search ended.
        
    Returns:
        List of node IDs representing the path from origin to goal.
    """
    path = [goal]
    while goal in came_from:
        goal = came_from[goal]
        path.append(goal)
    return path[::-1]  # Reverse the path so that it starts at the origin.

# -----------------------------------------------------------------------------
# depth_limited_dfs:
# -----------------------------------------------------------------------------
def depth_limited_dfs(current, destinations, edges, limit, visited, came_from, nodes_generated):
    """
    Performs a recursive depth-first search up to a fixed depth limit.
    
    Args:
        current: The current node being explored.
        destinations: List of destination node IDs.
        edges: Dictionary mapping nodes to lists of (neighbor, cost) tuples.
        limit: The remaining depth limit for the search.
        visited: Set of nodes already visited in this iteration.
        came_from: Dictionary storing the predecessor of each visited node.
        nodes_generated: Counter for the number of nodes generated so far.
        
    Returns:
        A tuple (result, nodes_generated, came_from)
            - result: The destination node if found; otherwise, None.
            - nodes_generated: Updated count of generated nodes.
            - came_from: The (possibly updated) predecessor dictionary.
    """
    # Check if the current node is one of the goals.
    if current in destinations:
        return current, nodes_generated, came_from
    # If the depth limit is reached, stop recursing.
    if limit == 0:
        return None, nodes_generated, came_from

    # Iterate over the neighbors of the current node in sorted order (for tie-breaking)
    for neighbor, _ in sorted(edges.get(current, []), key=lambda t: t[0]):
        if neighbor not in visited:
            visited.add(neighbor)
            came_from[neighbor] = current
            nodes_generated += 1
            # Recurse into the neighbor with a reduced depth limit.
            result, nodes_generated, came_from = depth_limited_dfs(
                neighbor, destinations, edges, limit - 1, visited, came_from, nodes_generated)
            # If a goal was found deeper down, return it immediately.
            if result is not None:
                return result, nodes_generated, came_from
    return None, nodes_generated, came_from

# -----------------------------------------------------------------------------
# iddfs_search:
# -----------------------------------------------------------------------------
def iddfs_search(origin, destinations, edges, max_depth=50):
    """
    Performs Iterative Deepening Depth-First Search (IDDFS) as the custom uninformed method.
    It calls depth_limited_dfs repeatedly with increasing depth limits until a destination is found.
    
    Args:
        origin: The starting node ID.
        destinations: List of destination node IDs.
        edges: Dictionary mapping nodes to (neighbor, cost) lists.
        max_depth: The maximum depth to search (default: 50).
        
    Returns:
        A tuple (goal, total_nodes_generated, path)
            - goal: The destination node reached (or None if not found).
            - total_nodes_generated: Total number of nodes generated during search.
            - path: List of node IDs representing the path from origin to goal.
    """
    total_nodes_generated = 0
    # Increase the depth limit from 0 up to max_depth.
    for limit in range(max_depth + 1):
        visited = set([origin])
        came_from = {}
        result, nodes_generated, came_from = depth_limited_dfs(
            origin, destinations, edges, limit, visited, came_from, 0)
        total_nodes_generated += nodes_generated
        if result is not None:
            return result, total_nodes_generated, reconstruct_path(came_from, result)
    return None, total_nodes_generated, []

# -----------------------------------------------------------------------------
# main:
# -----------------------------------------------------------------------------
def main():
    # Check for the correct number of command-line arguments.
    if len(sys.argv) != 2:
        print("Usage: python cus1_search.py <filename>")
        return

    filename = sys.argv[1]
    
    # Use the common input parser to obtain the graph data.
    # This ensures the file format is consistent with astar_search.py and gbfs_search.py.
    nodes, edges, origin, destinations = build_data(filename)
    
    # Execute the custom uninformed search using IDDFS.
    goal, count, path = iddfs_search(origin, destinations, edges, max_depth=50)

    # Print the results in a standard format:
    # Print the filename and method "CUS1", then the found goal, the number of nodes generated, and the path.
    print(f"{filename} CUS1")
    if path:
        print(f"{goal} {count}")
        print(" -> ".join(map(str, path)))
    else:
        print("No path found")

if __name__ == "__main__":
    main()
