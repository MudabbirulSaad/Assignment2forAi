# input_parser.py
# This module reads an input file (here called "input_data.txt") containing the graph data.
# It splits the file into meaningful sections (Nodes, Edges, Origin, Destinations)
# and then parses each section into Python data structures that our program can use.

def read_file(filename):
    """
    Opens the file and returns a list of non-empty lines with extra spaces removed.
    
    :param filename: A string representing the name (or path) of the file.
    :return: A list of cleaned-up lines from the file.
    """
    with open(filename, "r") as file:
        # Read each line, strip extra whitespace, and ignore any empty lines.
        lines = [line.strip() for line in file if line.strip()]
    return lines

def split_sections(lines):
    """
    Splits the list of lines into sections using headers (lines ending with ":").
    
    :param lines: A list of strings from the file.
    :return: A dictionary where each key is a section name (without the colon) and 
             the value is a list of lines belonging to that section.
    """
    sections = {}
    current_key = None
    for line in lines:
        # When a line ends with ":", it denotes a new section header.
        if line.endswith(":"):
            current_key = line.rstrip(":")  # Remove the colon to get the section name.
            sections[current_key] = []       # Create an empty list for this section.
        elif current_key:
            # Add the current line to the list corresponding to the current section.
            sections[current_key].append(line)
    return sections

def parse_nodes(node_lines):
    """
    Parses the "Nodes:" section. Each line is expected in the format:
        "1: (4,1)"
    where 1 is the node ID and (4,1) are the x and y coordinates.
    
    :param node_lines: List of lines from the "Nodes:" section.
    :return: A dictionary mapping node IDs to coordinate tuples, e.g., {1: (4, 1)}.
    """
    nodes = {}
    for line in node_lines:
        node_id_str, coord_str = line.split(":")
        node_id = int(node_id_str.strip())      # Convert the node ID to an integer.
        coord_str = coord_str.strip().strip("()")  # Remove spaces and parentheses.
        x_str, y_str = coord_str.split(",")        # Split the coordinate string.
        nodes[node_id] = (int(x_str), int(y_str))   # Store the node with its coordinates.
    return nodes

def parse_edges(edge_lines):
    """
    Parses the "Edges:" section. Each line is expected in the format:
        "(2,1): 4"
    meaning an edge from node 2 to node 1 with a cost of 4.
    
    :param edge_lines: List of lines from the "Edges:" section.
    :return: A dictionary where each key is a source node and its value is a list
             of tuples (destination, cost). The list is sorted by the destination node
             (for tie-breaking purposes).
    """
    edges = {}
    for line in edge_lines:
        edge_part, cost_str = line.split(":")
        cost = int(cost_str.strip())           # Convert the cost to an integer.
        edge_part = edge_part.strip().strip("()")  # Remove extra spaces and parentheses.
        from_str, to_str = edge_part.split(",")    # Split into source and destination.
        from_node, to_node = int(from_str), int(to_str)
        # If this source node hasn't been seen before, add it with an empty list.
        if from_node not in edges:
            edges[from_node] = []
        # Append the (destination, cost) tuple to the source node's list.
        edges[from_node].append((to_node, cost))
    # Sort the list of edges for each node by destination node for consistent tie-breaking.
    for from_node in edges:
        edges[from_node] = sorted(edges[from_node], key=lambda t: t[0])
    return edges

def parse_origin(origin_lines):
    """
    Parses the "Origin:" section, which is assumed to contain a single line.
    
    :param origin_lines: A list with one string representing the origin node.
    :return: The origin node as an integer.
    """
    return int(origin_lines[0].strip())

def parse_destinations(dest_lines):
    """
    Parses the "Destinations:" section. The destinations are in a single line separated by semicolons.
    
    :param dest_lines: A list with one string from the "Destinations:" section.
    :return: A list of integers representing the destination nodes.
    """
    return [int(item.strip()) for item in dest_lines[0].split(";")]

def build_data(filename):
    """
    Combines the steps to read the file, split it into sections, and parse each section.
    
    :param filename: The name or path of the input file.
    :return: A tuple (nodes, edges, origin, destinations) containing:
             - nodes: a dictionary of node coordinates,
             - edges: a dictionary of edges,
             - origin: the starting node,
             - destinations: a list of destination nodes.
    """
    lines = read_file(filename)
    sections = split_sections(lines)
    nodes = parse_nodes(sections.get("Nodes", []))
    edges = parse_edges(sections.get("Edges", []))
    origin = parse_origin(sections.get("Origin", []))
    destinations = parse_destinations(sections.get("Destinations", []))
    return nodes, edges, origin, destinations

# When you run this module by itself, it will load and print the data from the input file.
if __name__ == "__main__":
    filename = "input_data.txt"  # This should be the file you created with your graph data.
    nodes, edges, origin, destinations = build_data(filename)
    print("Parsed Nodes:", nodes)
    print("Parsed Edges:", edges)
    print("Origin:", origin)
    print("Destinations:", destinations)
