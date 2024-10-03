import java.util.*;

class GraphBestFS {
    private int vertices; // Number of vertices
    private LinkedList<Node>[] adjList; // Adjacency list to store nodes with weights

    // Node class to store vertex and cost (used for priority in Best-First Search)
    static class Node implements Comparable<Node> {
        int vertex;
        int cost;

        public Node(int vertex, int cost) {
            this.vertex = vertex;
            this.cost = cost;
        }

        // Comparison based on cost for priority queue
        public int compareTo(Node other) {
            return Integer.compare(this.cost, other.cost);
        }
    }

    // Constructor to initialize the graph
    public GraphBestFS(int vertices) {
        this.vertices = vertices;
        adjList = new LinkedList[vertices];
        for (int i = 0; i < vertices; i++) {
            adjList[i] = new LinkedList<>();
        }
    }

    // Method to add an edge with a weight between two vertices
    public void addEdge(int source, int destination, int cost) {
        adjList[source].add(new Node(destination, cost));
        // For undirected graph, uncomment the next line
        // adjList[destination].add(new Node(source, cost));
    }

    // Best-First Search (Greedy)
    public void bestFirstSearch(int start, int goal) {
        boolean[] visited = new boolean[vertices]; // Mark all vertices as unvisited
        PriorityQueue<Node> pq = new PriorityQueue<>(); // Priority queue to select the minimum cost edge

        // Start with the source node
        pq.add(new Node(start, 0));

        System.out.println("Best-First Search traversal from " + start + " to " + goal + ":");

        // Loop until the priority queue is empty
        while (!pq.isEmpty()) {
            // Get the vertex with the least cost
            Node current = pq.poll();
            int vertex = current.vertex;

            if (!visited[vertex]) {
                System.out.print(vertex + " ");
                visited[vertex] = true;

                // If we reach the goal, terminate
                if (vertex == goal) {
                    System.out.println("\nGoal " + goal + " reached.");
                    return;
                }

                // Traverse all neighbors
                for (Node neighbor : adjList[vertex]) {
                    if (!visited[neighbor.vertex]) {
                        pq.add(new Node(neighbor.vertex, neighbor.cost)); // Add to the queue based on cost
                    }
                }
            }
        }
    }

    // Self-check method for Best-First Search
    public static void selfCheck() {
        GraphBestFS g = new GraphBestFS(6); // Create a graph with 6 vertices

        // Add edges with weights (cost)
        g.addEdge(0, 1, 2);
        g.addEdge(0, 2, 4);
        g.addEdge(1, 2, 1);
        g.addEdge(1, 3, 7);
        g.addEdge(2, 4, 3);
        g.addEdge(3, 5, 1);
        g.addEdge(4, 3, 2);
        g.addEdge(4, 5, 5);

        // Best-First Search from vertex 0 to 5
        // Expected path: 0 -> 1 -> 2 -> 4 -> 3 -> 5 (depending on cost)
        System.out.println("\nRunning self-check for Best-First Search...");
        g.bestFirstSearch(0, 5);
    }

    // Main method to test Best-First Search
    public static void main(String[] args) {
        // Running self-check
        selfCheck();
    }
}
