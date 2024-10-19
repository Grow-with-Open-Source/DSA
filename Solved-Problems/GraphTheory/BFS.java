import java.util.*;

// Class to represent a graph
class Graph {
    private int vertices; // Number of vertices
    private LinkedList<Integer>[] adjList; // Adjacency list for storing graph

    // Constructor to initialize the graph
    public Graph(int vertices) {
        this.vertices = vertices;
        adjList = new LinkedList[vertices];
        for (int i = 0; i < vertices; i++) {
            adjList[i] = new LinkedList<>();
        }
    }

    // Method to add an edge between two vertices
    public void addEdge(int source, int destination) {
        adjList[source].add(destination);
        // For undirected graph, uncomment the following line
        // adjList[destination].add(source);
    }

    // BFS algorithm starting from the given source node
    public void BFS(int start) {
        // Boolean array to mark visited vertices
        boolean[] visited = new boolean[vertices];

        // Queue for BFS
        Queue<Integer> queue = new LinkedList<>();

        // Mark the start node as visited and enqueue it
        visited[start] = true;
        queue.add(start);

        System.out.println("BFS traversal starting from vertex " + start + ":");

        // Loop until the queue is empty
        while (!queue.isEmpty()) {
            // Dequeue a vertex and print it
            int current = queue.poll();
            System.out.print(current + " ");

            // Get all adjacent vertices of the dequeued vertex
            // If an adjacent vertex hasn't been visited, mark it visited and enqueue it
            for (int neighbor : adjList[current]) {
                if (!visited[neighbor]) {
                    visited[neighbor] = true;
                    queue.add(neighbor);
                }
            }
        }
    }

    // Self-check method to verify the BFS functionality
    public static void selfCheck() {
        Graph g = new Graph(5); // Create a graph with 5 vertices (0 to 4)
        
        // Adding edges
        g.addEdge(0, 1);
        g.addEdge(0, 4);
        g.addEdge(1, 2);
        g.addEdge(1, 3);
        g.addEdge(1, 4);
        g.addEdge(2, 3);
        g.addEdge(3, 4);

        // Expected BFS traversal from vertex 0: 0 1 4 2 3
        System.out.println("\nRunning self-check for BFS...");
        g.BFS(0);  // Should print the correct BFS traversal


    }

    // Main method to test the implementation
    public static void main(String[] args) {
        // Running self-checks
        selfCheck();
    }
}
