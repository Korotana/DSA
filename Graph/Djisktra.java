package Graph;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;



public class Djisktra {

    public PriorityQueue<Vertex> queue ;

    public Djisktra() {
        this.queue = new PriorityQueue<>();
    }


     void djisktra(ArrayList<ArrayList<Vertex>> edges, int numVertices, int source, int[] distance, HashSet<Integer> fin){

        Arrays.fill(distance,Integer.MAX_VALUE);

        queue.add(new Vertex(source,0));

        //distance of source from itself is 0
        distance[source] = 0;

        while (fin.size() != numVertices) {
            if (queue.isEmpty()) return;

            Vertex u = queue.remove();

            if (fin.contains(u.dest)) continue;

            fin.add(u.dest);

            int edist = -1;
            int tempdist = -1;

            for (int i = 0; i < edges.get(u.dest).size(); i++) {

                Vertex v = edges.get(u.dest).get(i);

                if (!fin.contains(v.dest)){
                    edist = v.weight;
                    tempdist = edist + distance[u.dest];

                    if (tempdist < distance[v.dest]) distance[v.dest] = tempdist;

                    queue.add(new Vertex(v.dest,distance[v.dest]));
                }

            }

        }
    }


    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String temp = "";

        while ((temp = br.readLine()) != null){
            StringTokenizer token = new StringTokenizer(temp);

            int numVertices = Integer.parseInt(token.nextToken());
            int edges = Integer.parseInt(token.nextToken());
            int queries = Integer.parseInt(token.nextToken());
            int source = Integer.parseInt(token.nextToken());

            if (numVertices+edges+queries+source==0) break;

            ArrayList<ArrayList<Vertex>> startvetex = new ArrayList<>();

            for (int i = 0; i < numVertices; i++) {
                startvetex.add(new ArrayList<Vertex>());
            }

            for (int i = 0; i < edges; i++) {
                token = new StringTokenizer(br.readLine());
                int start = Integer.parseInt(token.nextToken());
                int dest = Integer.parseInt(token.nextToken());
                int weight = Integer.parseInt(token.nextToken());
                startvetex.get(start).add(new Vertex(dest,weight));
            }
            int[] allqueries = new int[queries];
            for (int i = 0; i < queries; i++) {
                token = new StringTokenizer(br.readLine());
                allqueries[i] = Integer.parseInt(token.nextToken());
            }

            int[] distance = new int[numVertices];
            HashSet<Integer> fianl = new HashSet<>();


            Djisktra d = new Djisktra();
            d.djisktra(startvetex,numVertices,source,distance,fianl);


            for (int i = 0; i < allqueries.length; i++){
                if (distance[allqueries[i]] == Integer.MAX_VALUE) System.out.println("Impossible");
                else System.out.println(distance[allqueries[i]]);
            }
        }
    }
}

class Vertex implements Comparable<Vertex>{

    int dest;
    int weight;

    public Vertex(int dest, int weight) {
        this.dest = dest;
        this.weight = weight;
    }

    @Override
    public int compareTo(Vertex v2) {
        return Integer.compare(this.weight, v2.weight);
    }
}