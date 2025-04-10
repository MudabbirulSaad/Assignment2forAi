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
└── input_data.txt        # Example input data file
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
| Test Cases                        | ❌ Pending  | Create 10+ test cases with varying complexity         |
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
- COS30019 Assignment 2A Specification
