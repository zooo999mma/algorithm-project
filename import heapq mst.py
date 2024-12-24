import heapq

def prims_algorithm(graph, start):
    mst = []  # List to store the MST edges
    visited = set()
    min_heap = [(0, start, None)]  # (cost, node, parent)
    
    while min_heap:
        cost, node, parent = heapq.heappop(min_heap)
        if node not in visited:
            visited.add(node)
            if parent is not None:
                mst.append((parent, node, cost))
            
            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (weight, neighbor, node))
    
    return mst

# Example usage
graph = {
    'A': [('B', 2), ('D', 1)],
    'B': [('A', 2), ('D', 3), ('E', 4)],
    'C': [('E', 5)],
    'D': [('A', 1), ('B', 3), ('E', 1)],
    'E': [('B', 4), ('C', 5), ('D', 1)],
}
mst = prims_algorithm(graph, 'A')
print("Minimum Spanning Tree:", mst)