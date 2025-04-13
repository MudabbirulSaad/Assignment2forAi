# Algorithm Performance Analysis

## Overview

This report presents the performance analysis of six search algorithms implemented for route finding across ten different test cases. The algorithms evaluated are:

1. BFS (Breadth-First Search)
2. DFS (Depth-First Search)
3. GBFS (Greedy Best-First Search)
4. AS (A* Search)
5. CUS1 (Iterative Deepening DFS)
6. CUS2 (Bidirectional Weighted A*)

## Summary of Results

| Method | Avg Time | Avg Nodes | Success Rate | Avg Path Length |
|:-------|:---------|----------:|:-------------|----------------:|
| BFS    | 0.000000s | 18 | 100.0% | 5.2 |
| DFS    | 0.000000s | 13 | 100.0% | 9.8 |
| GBFS   | 0.000100s | 6 | 100.0% | 5.3 |
| AS     | 0.000100s | 15 | 100.0% | 5.4 |
| CUS1   | 0.000000s | 58 | 100.0% | 5.8 |
| CUS2   | 0.000423s | 55 | 100.0% | 5.5 |

## Key Findings

### 1. Algorithm Efficiency (Nodes Generated)

- **GBFS** was the most efficient algorithm in terms of nodes generated, averaging only 6 nodes per test case.
- **DFS** was also efficient with an average of 13 nodes, though this comes at the cost of optimal path finding.
- **CUS1** (IDDFS) generated the most nodes (58 on average), which aligns with its iterative approach that repeats searches at increasing depths.
- **CUS2** (Bidirectional Weighted A*) generated 55 nodes on average, which is higher than simpler algorithms but includes nodes from both forward and backward searches.

### 2. Path Optimality

- **DFS** produced the least optimal paths with an average length of 9.8, significantly higher than other algorithms.
- **BFS** provided optimal paths for unweighted graphs with an average length of 5.2.
- **AS** (A*) and **CUS2** (Bidirectional Weighted A*) produced similar average path lengths (5.4 and 5.5 respectively), confirming near-optimality of CUS2.
- **GBFS** achieved a good average path length (5.3) despite using only a heuristic, suggesting the test cases had well-aligned heuristic and cost functions.

### 3. Execution Time

- All algorithms performed very efficiently, with most completing in under 0.001 seconds.
- The execution times are too small to make significant comparisons on these test cases.
- **CUS2** had a slightly higher average time (0.000423s), which is expected given its more complex bidirectional approach.

### 4. Success Rate

- All algorithms achieved a 100% success rate across all test cases, indicating that all test cases had at least one valid path to a destination.

## Test Case Analysis

### Test Case Complexity

- **Test Case 5** appeared to be the most challenging, with CUS1 generating 192 nodes, the highest observed count.
- **Test Case 6** also showed higher complexity, requiring 103 nodes for CUS1.
- **Test Case 10** was relatively simpler, with GBFS finding a solution with only 3 nodes.

### Algorithm Performance by Test Case

1. **Simple Path Finding (Test Case 1, 4, 8, 9, 10)**:
   - GBFS and DFS performed exceptionally well in node efficiency
   - BFS consistently found optimal paths

2. **Complex Navigation (Test Case 3, 5, 6)**:
   - All algorithms found paths, but with varying node counts
   - DFS paths were significantly longer than optimal in these cases
   - A* maintained consistent performance in finding optimal paths

3. **Multiple Destinations (Test Case 2, 7)**:
   - GBFS sometimes led to different destinations than other algorithms
   - CUS2 consistently found optimal paths to appropriate destinations

## Conclusions

1. **Best Overall Performance**: GBFS showed the best balance between efficiency (nodes generated) and path quality for these test cases.

2. **Best for Optimal Paths**: A* consistently found optimal paths with reasonable efficiency.

3. **Most Reliable**: BFS and A* provided the most consistent performance across all test cases.

4. **Trade-offs**:
   - DFS: Highly efficient in node generation but produces significantly longer paths
   - GBFS: Most efficient in node generation with good path quality, but no guarantee of optimality
   - CUS1 (IDDFS): Higher node generation but guarantees optimal paths with modest memory usage
   - CUS2 (BDWA): Higher implementation complexity but balanced performance with near-optimal paths

5. **Recommendations**:
   - For simple path finding with optimal paths: Use BFS
   - For best overall efficiency: Use GBFS
   - For guaranteed optimal paths in larger graphs: Use A*
   - For memory-constrained environments: Consider CUS1 (IDDFS)
   - For complex, large-scale problems: CUS2 (BDWA) would likely show more significant advantages

## Limitations of Analysis

1. The test cases were relatively small, resulting in execution times too brief for meaningful comparison.
2. All algorithms achieved 100% success, suggesting the test cases might not be challenging enough to highlight differences in robustness.
3. The time measurements have limited precision and may not accurately reflect the true computational complexity differences.

## Future Work

1. Test with larger, more complex graphs to better demonstrate algorithm performance differences.
2. Measure memory usage to evaluate space complexity alongside time complexity.
3. Introduce additional metrics like expanded/visited node ratio to better understand search efficiency.
4. Implement variable heuristic weights in CUS2 to explore the trade-off between optimality and efficiency. 