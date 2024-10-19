import java.util.*;

class GraphDFS {
    private int vertices; // Number of vertices
    private LinkedList<Integer>[] adjList; // Adjacency list for graph representation

    // Constructor to initialize graph
    public GraphDFS(int vertices) {
        this.vertices = vertices;
        adjList = new LinkedList[vertices];
        for (int i = 0; i < vertices; i++) {
            adjList[i] = new LinkedList<>();
        }
    }

    // Method to add an edge between two vertices
    public void addEdge(int source, int destination) {
        adjList[source].add(destination);
        // For undirected graph, uncomment the next line
        // adjList[destination].add(source);
    }

    // DFS algorithm
    private void DFSUtil(int vertex, boolean[] visited) {
        // Mark the current node as visited and print it
        visited[vertex] = true;
        System.out.print(vertex + " ");

        // Recur for all adjacent vertices of the current vertex
        for (int neighbor : adjList[vertex]) {
            if (!visited[neighbor]) {
                DFSUtil(neighbor, visited);
            }
        }
    }

    // Public method to initiate DFS traversal
    public void DFS(int start) {
        boolean[] visited = new boolean[vertices]; // Mark all vertices as unvisited
        System.out.println("DFS traversal starting from vertex " + start + ":");
        DFSUtil(start, visited); // Start DFS from the given node
    }

    // Self-check method to test DFS functionality
    public static void selfCheck() {
        GraphDFS g = new GraphDFS(5); // Create a graph with 5 vertices

        // Add edges
        g.addEdge(0, 1);
        g.addEdge(0, 4);
        g.addEdge(1, 2);
        g.addEdge(1, 3);
        g.addEdge(1, 4);
        g.addEdge(2, 3);
        g.addEdge(3, 4);

        // Expected DFS traversal from vertex 0: 0 1 2 3 4
        System.out.println("\nRunning self-check for DFS...");
        g.DFS(0);

    }

    // Main method to test DFS
    public static void main(String[] args) {
        // Running self-checks
        selfCheck();
    }
}
