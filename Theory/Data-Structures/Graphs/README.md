## 5. Graphs
A **Graph** is a collection of vertices (nodes) and edges (connections between nodes) representing networks.

### Key Characteristics
- **Directed** vs **Undirected**: Directed graphs have edges with direction.
- **Weighted** vs **Unweighted**: Weighted graphs assign values to edges.

### Common Representations
- **Adjacency Matrix**: A 2D array where cells indicate edge presence.
  - Space Complexity: \(O(V^2)\)
- **Adjacency List**: Each vertex has a list of adjacent vertices.
  - Space Complexity: \(O(V + E)\)

### Common Operations
- **Traversal**:
  - **Breadth-First Search (BFS)**: Level-order traversal, useful for finding shortest paths in unweighted graphs.
  - **Depth-First Search (DFS)**: Visits nodes as deep as possible before backtracking, useful for pathfinding.
- **Shortest Path Algorithms**:
  - **Dijkstra's Algorithm**: Finds shortest paths from a single source in a weighted graph.
  - **Floyd-Warshall**: All-pairs shortest paths.
- **Minimum Spanning Tree (MST)**:
  - **Kruskal's and Prim's Algorithms**: Find the minimum cost to connect all nodes in a weighted graph.

### Applications
- **Networks**: Routing algorithms in communication networks.
- **Social Networks**: Representing and analyzing relationships.
- **Web Crawling**: Link structure of websites.
- **Pathfinding**: Navigation systems and game AI.
- **Scheduling**: Task scheduling with dependencies.