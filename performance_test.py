import sys
import time
import os
import csv
from tabulate import tabulate
from collections import defaultdict

# Try to import the search methods
try:
    from methods.bfs_search import bfs
    from methods.dfs_search import dfs
    from methods.gbfs_search import gbfs
    from methods.astar_search import astar
    from methods.iddfs_search import iddfs
    from methods.bdwa_search import bdwa
    from input_parser import build_data
    from graph import Graph
except ImportError as e:
    print(f"Error importing modules: {e}")
    sys.exit(1)

def run_test(filename, method_name, method_func, *args):
    """Run a single test and measure performance"""
    start_time = time.time()
    goal, count, path = method_func(*args)
    end_time = time.time()
    execution_time = end_time - start_time
    path_length = len(path) - 1 if path else 0  # -1 because we count edges
    
    return {
        'test_case': os.path.basename(filename),
        'method': method_name,
        'execution_time': execution_time,
        'nodes_generated': count,
        'path_found': bool(path),
        'goal': goal if goal else "None",
        'path_length': path_length
    }

def main():
    # Define all test cases
    test_cases_dir = "test_cases"
    test_files = [os.path.join(test_cases_dir, f) for f in os.listdir(test_cases_dir) 
                 if f.endswith('.txt') and f.startswith('test_case')]
    
    # Sort test files numerically
    test_files.sort(key=lambda x: int(''.join(filter(str.isdigit, os.path.basename(x)))))
    
    # Define all methods
    methods = {
        'BFS': bfs,
        'DFS': dfs,
        'GBFS': gbfs,
        'AS': astar,
        'CUS1': iddfs,
        'CUS2': bdwa
    }
    
    results = []
    
    # Run all tests
    for filename in test_files:
        print(f"Testing {filename}...")
        try:
            # Parse the input file
            node_pos, edges, origin, destinations = build_data(filename)
            
            # Run each method
            for method_name, method_func in methods.items():
                print(f"  Running {method_name}...")
                
                # Different methods require different arguments
                if method_name in ['GBFS', 'AS', 'CUS2']:
                    result = run_test(filename, method_name, method_func, 
                                     origin, destinations, edges, node_pos)
                else:
                    result = run_test(filename, method_name, method_func, 
                                     origin, destinations, edges)
                
                results.append(result)
                print(f"    Completed: {result['execution_time']:.4f}s, {result['nodes_generated']} nodes")
                
        except Exception as e:
            print(f"Error processing {filename}: {e}")
    
    # Save results to CSV
    with open('performance_results.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=results[0].keys())
        writer.writeheader()
        writer.writerows(results)
    
    # Print summarized results
    print("\n=== PERFORMANCE RESULTS ===")
    
    # Group results by test case
    test_case_results = defaultdict(list)
    for result in results:
        test_case_results[result['test_case']].append(result)
    
    # Calculate averages across all tests for each method
    method_summary = defaultdict(lambda: {'time': 0, 'nodes': 0, 'success': 0, 'total': 0, 'path_length': 0})
    
    for result in results:
        method = result['method']
        method_summary[method]['time'] += result['execution_time']
        method_summary[method]['nodes'] += result['nodes_generated']
        method_summary[method]['success'] += 1 if result['path_found'] else 0
        method_summary[method]['total'] += 1
        if result['path_found']:
            method_summary[method]['path_length'] += result['path_length']
    
    # Calculate averages
    for method, data in method_summary.items():
        data['avg_time'] = data['time'] / data['total']
        data['avg_nodes'] = data['nodes'] / data['total']
        data['success_rate'] = data['success'] / data['total'] * 100
        data['avg_path_length'] = data['path_length'] / data['success'] if data['success'] > 0 else 0
    
    # Print summarized results
    summary_table = []
    for method, data in method_summary.items():
        summary_table.append([
            method,
            f"{data['avg_time']:.6f}s",
            int(data['avg_nodes']),
            f"{data['success_rate']:.1f}%",
            f"{data['avg_path_length']:.1f}"
        ])
    
    print(tabulate(summary_table, 
                 headers=['Method', 'Avg Time', 'Avg Nodes', 'Success Rate', 'Avg Path Length'],
                 tablefmt='pipe'))
    
    # Print per test case results
    print("\n=== TEST CASE DETAILS ===")
    for test_case, test_results in test_case_results.items():
        print(f"\nTest Case: {test_case}")
        
        detail_table = []
        for result in test_results:
            detail_table.append([
                result['method'],
                f"{result['execution_time']:.6f}s",
                result['nodes_generated'],
                "Yes" if result['path_found'] else "No",
                result['path_length'] if result['path_found'] else "-"
            ])
        
        print(tabulate(detail_table, 
                     headers=['Method', 'Time', 'Nodes', 'Found', 'Path Length'],
                     tablefmt='pipe'))
    
    print("\nResults saved to performance_results.csv")

if __name__ == "__main__":
    main() 