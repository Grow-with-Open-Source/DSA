import java.util.ArrayList;

public class BellmanFord {
    public static void main(String[] args) {
        int vertex = 5;
        @SuppressWarnings("unchecked")
        ArrayList<Edge>[] graph = new ArrayList[vertex];

        create(graph);
        bf(graph, 0, vertex);

    }

    static class Edge {
        int src;
        int dest;
        int weight;

        public Edge(int s, int d, int w) {
            this.src = s;
            this.dest = d;
            this.weight = w;
        }
    }

    public static void create(ArrayList<Edge> graph[]) {
        for (int i = 0; i < graph.length; i++) {
            graph[i] = new ArrayList<>();
        }
        graph[0].add(new Edge(0, 1, 2));
        graph[0].add(new Edge(0, 2, 4));

        graph[1].add(new Edge(1, 2, -4));

        graph[2].add(new Edge(2, 3, 2));

        graph[3].add(new Edge(3, 4, 4));

        graph[4].add(new Edge(4, 1, -1));

    }

    public static void bf(ArrayList<Edge> graph[], int src, int V) {
        int[] dis = new int[V];
        for (int i = 0; i < V; i++) {
            if (i != src) {
                dis[i] = Integer.MAX_VALUE;
            }
        }

        for (int k = 0; k < V - 1; k++) {
            for (int j = 0; j < V; j++) {
                for (int i = 0; i < graph[i].size(); i++) {
                    Edge e = graph[j].get(i);
                    int u = e.src;
                    int v = e.dest;

                    if (dis[u] < Integer.MAX_VALUE && dis[u] + e.weight < dis[v]) {
                        dis[v] = dis[u] + e.weight;
                    }

                }
            }

        }

        for (int i = 0; i < dis.length; i++) {
            System.err.println(dis[i] + " ");

        }
    }
}
