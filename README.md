# Tree-Based Search Algorithms for Route Finding

## Overview
This repository contains an implementation of various search algorithms for the route finding problem, developed as part of COS30019 - Introduction to Artificial Intelligence (Assignment 2, Part A). The goal is to find optimal paths (with lowest cost) between an origin node and one or more destination nodes on a 2D graph.

## Project Structure
```
├── bfs_search.py         # Breadth-First Search implementation
├── dfs_search.py         # Depth-First Search implementation
├── gbfs_search.py        # Greedy Best-First Search implementation
├── astar_search.py       # A* Search implementation
├── graph.py              # Graph class for storing and managing graph data
├── input_parser.py       # Functions for parsing input files
├── search.py             # Unified command-line interface for all search algorithms
├── input_data.txt        # Example input data file
└── test_cases/           # Test cases directory
    ├── test_case1.txt    # City Transportation Network (Downtown to Airport)
    ├── test_case2.txt    # Emergency Response Network (Ambulance Routing)
    └── test_case3.txt    # Warehouse Robot Navigation System
```

## Input File Format
Input files should follow this format:
```
Nodes:
1: (x1,y1)
2: (x2,y2)
...
Edges:
(from,to): cost
...
Origin:
start_node
Destinations:
goal_node1; goal_node2; ...
```

## Input Parser Details
The `input_parser.py` module provides a robust system for parsing test case files:

1. **File Reading**: The `read_file` function reads a file and filters out empty lines.
2. **Section Splitting**: The `split_sections` function organizes lines into sections (Nodes, Edges, Origin, Destinations).
3. **Node Parsing**: The `parse_nodes` function extracts node IDs and their (x,y) coordinates.
4. **Edge Parsing**: The `parse_edges` function processes edge definitions, creating a dictionary of connections with costs.
5. **Origin & Destination Parsing**: The `parse_origin` and `parse_destinations` functions extract start and goal nodes.
6. **Data Integration**: The `build_data` function integrates all parsing functions to return structured data.

The parser is designed to handle comments (lines starting with #) and malformed lines gracefully, ensuring robust processing of input data. Node definitions can include descriptive comments, which are preserved for human-readable output in the search results.

## Search Algorithms
The following search algorithms have been implemented:

- ✅ **BFS (Breadth-First Search)** - Uninformed: Expands all nodes at a given depth before moving to the next level
  - Implementation: Uses a queue (FIFO) to maintain frontier nodes
  - Characteristics: Complete, optimal for unweighted graphs, but can be inefficient for large graphs
  - Time Complexity: O(b^d) where b is branching factor and d is depth

- ✅ **DFS (Depth-First Search)** - Uninformed: Explores as far as possible along each branch before backtracking
  - Implementation: Uses a stack (LIFO) to maintain frontier nodes
  - Characteristics: Not complete, not optimal, but memory-efficient
  - Time Complexity: O(b^m) where b is branching factor and m is maximum depth

- ✅ **GBFS (Greedy Best-First Search)** - Informed: Selects the node that appears closest to the goal
  - Implementation: Uses a priority queue with Euclidean distance heuristic
  - Characteristics: Not optimal, but can be efficient when heuristic is good
  - Time Complexity: O(b^m) where b is branching factor and m is maximum depth

- ✅ **A* Search** - Informed: Combines path cost and heuristic for optimal path finding
  - Implementation: Uses a priority queue with f(n) = g(n) + h(n)
  - Characteristics: Complete, optimal when heuristic is admissible
  - Time Complexity: O(b^d) where b is branching factor and d is depth of the solution
  - Memory Requirement: Higher than other algorithms

- ✅ **CUS1 (Iterative Deepening DFS)** - Uninformed: Combines benefits of BFS and DFS
  - Implementation: Uses depth-limited DFS with increasing depth limits
  - Characteristics: Complete, optimal for unweighted graphs, and memory-efficient
  - Time Complexity: O(b^d) where b is branching factor and d is depth of the solution
  - Benefits: Guarantees finding the shortest path while using minimal memory

- ❌ **CUS2 (Custom Search 2)** - Informed: Find shortest path with least moves (self-researched)

All search algorithms are implemented to handle the following requirements:
- **Node Expansion Order**: When all else is equal, nodes are expanded in ascending order by ID
- **Chronological Order**: When nodes have equal priority, they're expanded in the order they were added
- **Path Tracking**: Each algorithm tracks the complete path from origin to goal

The implementation allows seamless switching between algorithms through the unified `search.py` interface.

## Implementation Roadmap

| Feature                           | Status      | Description                                           |
|-----------------------------------|-------------|-------------------------------------------------------|
| Basic Infrastructure              | ✅ Complete | Input parsing, graph representation                    |
| BFS Implementation                | ✅ Complete | Breadth-First Search with proper node expansion order |
| DFS Implementation                | ✅ Complete | Depth-First Search with proper node expansion order   |
| GBFS Implementation               | ✅ Complete | Greedy Best-First Search with Euclidean heuristic     |
| A* Search Implementation          | ✅ Complete | A* Search with Euclidean heuristic and path costs     |
| Custom Search 1                   | ✅ Complete | Iterative Deepening DFS - memory efficient approach   |
| Custom Search 2                   | ❌ Pending  | Self-researched informed search algorithm             |
| Unified Command Interface         | ✅ Complete | Common interface through search.py                    |
| Test Cases                        | ✅ Complete | Created 3 test cases with varying complexity          |
| Performance Analysis              | ❌ Pending  | Compare algorithm performance metrics                 |
| Report                            | ❌ Pending  | Create comprehensive report as per requirements       |

## Usage
### Running a Search Algorithm
To run a search algorithm on an input file:

```bash
python search.py <filename> <method>
```

Where:
- `<filename>` is the path to the input file
- `<method>` is one of: BFS, DFS, GBFS, AS, CUS1

### Example
```bash
python search.py input_data.txt BFS
python search.py test_cases/test_case1.txt GBFS
python search.py test_cases/test_case2.txt AS
python search.py test_cases/test_case3.txt CUS1
```

### Output Format
The output follows the format specified in the assignment:
```
filename method
goal number_of_nodes
path
```

Where:
- `goal` is the goal node reached
- `number_of_nodes` is the number of nodes created during search
- `path` is the sequence of moves in the solution (e.g., `1 -> 2 -> 3`)

## Test Cases
Three real-world scenario test cases have been developed to evaluate the algorithms:

1. **City Transportation Network** (test_case1.txt):
   - **Scenario**: Finding the optimal route from downtown to the airport
   - **Context**: A traveler needs to navigate from Downtown Central Station to the Airport Terminal
   - **Constraints**: Various road distances (in km) with different route options
   - **Challenge**: Finding the shortest path through a city road network with multiple possible routes

2. **Emergency Response Network** (test_case2.txt):
   - **Scenario**: Ambulance routing to available hospitals during an emergency
   - **Context**: Emergency services need to find the fastest route from an accident site to either of two hospitals
   - **Constraints**: Traffic conditions affect travel times (measured in minutes)
   - **Challenge**: Multiple destinations with time-critical routing decisions

3. **Warehouse Robot Navigation System** (test_case3.txt):
   - **Scenario**: Autonomous robot navigating through a warehouse
   - **Context**: A delivery robot must find its way from the Loading Bay to the Delivery Pickup Point
   - **Constraints**: Grid-like layout with fixed movement costs between connected locations
   - **Challenge**: Maze-like environment requiring efficient path planning

All test cases are compatible with both the currently implemented algorithms and future custom algorithms.

## Assignment Requirements
- Node expansion order: When all else is equal, nodes should be expanded in ascending order
- Chronological order: When nodes on different branches have equal priority, expand in the order they were added
- Output format: Follow the specified format for all search algorithms

## Contributors (Swinburne Student IDs)
- 105281389
- 104654906
- 104071152
- 103825785

## License
This project is submitted as part of the COS30019 - Introduction to AI course assignment.

## References

1. Russell, S., & Norvig, P. (2020). *Artificial Intelligence: A Modern Approach* (4th ed.). Pearson. [http://aima.cs.berkeley.edu/](http://aima.cs.berkeley.edu/)

2. Hart, P. E., Nilsson, N. J., & Raphael, B. (1968). A Formal Basis for the Heuristic Determination of Minimum Cost Paths. *IEEE Transactions on Systems Science and Cybernetics*, 4(2), 100-107. [https://doi.org/10.1109/TSSC.1968.300136](https://doi.org/10.1109/TSSC.1968.300136)

3. Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). *Introduction to Algorithms* (3rd ed.). MIT Press. [https://mitpress.mit.edu/books/introduction-algorithms-third-edition](https://mitpress.mit.edu/books/introduction-algorithms-third-edition)

4. Dechter, R., & Pearl, J. (1985). Generalized Best-First Search Strategies and the Optimality of A*. *Journal of the ACM*, 32(3), 505-536. [https://doi.org/10.1145/3828.3830](https://doi.org/10.1145/3828.3830)

5. Korf, R. E. (1985). Depth-first Iterative-Deepening: An Optimal Admissible Tree Search. *Artificial Intelligence*, 27(1), 97-109. [https://doi.org/10.1016/0004-3702(85)90084-0](https://doi.org/10.1016/0004-3702(85)90084-0)

6. LaValle, S. M. (2006). *Planning Algorithms*. Cambridge University Press. [http://planning.cs.uiuc.edu/](http://planning.cs.uiuc.edu/)

7. COS30019 Assignment 2A Specification, Swinburne University of Technology.
