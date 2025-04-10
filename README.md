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
    ├── test_case1.txt    # Test case with multiple possible paths
    ├── test_case2.txt    # Complex test with multiple destinations
    └── test_case3.txt    # Maze-like challenge with multiple paths
```

## Search Algorithms
The following search algorithms have been implemented:

- ✅ **BFS (Breadth-First Search)** - Uninformed: Expand all options one level at a time
- ✅ **DFS (Depth-First Search)** - Uninformed: Select one option, try it, go back when no more options
- ✅ **GBFS (Greedy Best-First Search)** - Informed: Use only the cost to reach the goal from current node
- ✅ **A* Search** - Informed: Use both the cost to goal and cost to current node
- ❌ **CUS1 (Custom Search 1)** - Uninformed: Find a path to reach the goal (self-researched)
- ❌ **CUS2 (Custom Search 2)** - Informed: Find shortest path with least moves (self-researched)

## Implementation Roadmap

| Feature                           | Status      | Description                                           |
|-----------------------------------|-------------|-------------------------------------------------------|
| Basic Infrastructure              | ✅ Complete | Input parsing, graph representation                    |
| BFS Implementation                | ✅ Complete | Breadth-First Search with proper node expansion order |
| DFS Implementation                | ✅ Complete | Depth-First Search with proper node expansion order   |
| GBFS Implementation               | ✅ Complete | Greedy Best-First Search with Euclidean heuristic     |
| A* Search Implementation          | ✅ Complete | A* Search with Euclidean heuristic and path costs     |
| Custom Search 1                   | ❌ Pending  | Self-researched uninformed search algorithm           |
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
- `<method>` is one of: BFS, DFS, GBFS, AS

### Example
```bash
python search.py input_data.txt BFS
python search.py test_cases/test_case1.txt GBFS
python search.py test_cases/test_case2.txt AS
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
Three different test cases have been developed to evaluate the algorithms:

1. **Test Case 1**: A simple graph with multiple paths to a single destination, designed to test basic path-finding capabilities.

2. **Test Case 2**: A more complex graph with multiple destinations, testing the algorithm's ability to find the most efficient path to any valid destination.

3. **Test Case 3**: A maze-like graph with many interconnected nodes, designed to challenge algorithmic efficiency and test handling of complex path decisions.

All test cases are compatible with both the currently implemented algorithms and future custom algorithms.

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
