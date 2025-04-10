# graph.py
# This module defines the Graph class, which stores the nodes and edges of the graph
# and provides a method to retrieve neighbors of a given node.

class Graph:
    def __init__(self, nodes, edges):
        """
        Initializes the graph with the provided nodes and edges.
        
        :param nodes: A dictionary mapping node IDs to coordinate tuples (x, y).
        :param edges: A dictionary mapping source node IDs to a list of tuples (destination, cost).
        """
        self.nodes = nodes  # Store node information.
        self.edges = edges  # Store edge information (connections between nodes).

    def get_neighbors(self, node):
        """
        Retrieves the neighbors of a given node.
        This function looks up the edges dictionary for the provided node.
        
        :param node: The node ID whose neighbors are required.
        :return: A list of tuples (neighbor, cost). Returns an empty list if the node has no outgoing edges.
        """
        return self.edges.get(node, [])

# The following integration example builds a Graph object using our input parser.
if __name__ == "__main__":
    # Import the build_data function from the input_parser module.
    from input_parser import build_data

    def build_graph(filename):
        """
        Reads the data from the input file using the input parser and creates a Graph object.
        
        :param filename: The name or path of the input file.
        :return: A tuple (graph_instance, origin, destinations) where graph_instance is a Graph object.
        """
        nodes, edges, origin, destinations = build_data(filename)
        graph_instance = Graph(nodes, edges)
        return graph_instance, origin, destinations

    filename = "input_data.txt"  # This is the file that contains your graph data.
    graph_instance, origin, destinations = build_graph(filename)
    print("Graph Nodes:", graph_instance.nodes)
    print("Graph Edges:", graph_instance.edges)
    print("Origin:", origin)
    print("Destinations:", destinations)
    print("Neighbors of Origin ({}): {}".format(origin, graph_instance.get_neighbors(origin)))
