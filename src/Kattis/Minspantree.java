package Kattis;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Minspantree {

    static class Edge implements Comparable<Edge>{
        int source;
        int destination;
        int weight;

        public Edge(int newsource, int newdestination, int newweight) {
            this.source = newsource;
            this.destination = newdestination;
            this.weight = newweight;
        }

        @Override
        public int compareTo(Edge o) {
            return weight - o.weight;
        }
    }

    static class couple implements Comparable<couple>{
        int first, second;


        public couple(Edge e) {
            this.first = Math.min(e.source,e.destination);
            this.second = Math.max(e.source,e.destination);
        }

        @Override
        public int compareTo(couple o) {
            if (first != o.first) return first - o.first;

            else return second - o.second;
        }
    }


    static class disJointSet{
        int[] parent;

        public disJointSet(int size) {
            parent = new int[size];
            for (int i = 0; i < size; i++)
                parent[i] = i;
        }

        int find(int x){
            if (parent[x] == x) return x;

            else return parent[x] = find(parent[x]);
        }

        void union(int e1, int e2){
            parent[find(e1)] = find(e2);
        }
    }


    public static void main(String[] args) throws Exception{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String temp="";
        while((temp = br.readLine()) != null) {
            StringTokenizer token = new StringTokenizer(temp);

            int numVertices = Integer.parseInt(token.nextToken());
            int numEdges = Integer.parseInt(token.nextToken());

            if (numEdges+numVertices == 0) {
                break;
            }

            PriorityQueue<Edge> queue = new PriorityQueue<>();

            for (int i = 0; i < numEdges; i++) {
                StringTokenizer tokenTemp = new StringTokenizer(br.readLine());
                int source = Integer.parseInt(tokenTemp.nextToken());
                int destination = Integer.parseInt(tokenTemp.nextToken());
                int weight = Integer.parseInt(tokenTemp.nextToken());
                queue.add(new Edge(source, destination, weight));
            }

            int cost = 0;
            disJointSet set = new disJointSet(numVertices);
            ArrayList<couple> edgePair = new ArrayList<>();

            while (!queue.isEmpty()) {
                Edge minimum = queue.poll();
                if (set.find(minimum.source) != set.find(minimum.destination)) {
                    cost += minimum.weight;

                    edgePair.add(new couple(minimum));
                    set.union(minimum.source, minimum.destination);
                    if (edgePair.size() == numVertices-1)
                        break;
                }
            }
            if (edgePair.size() != numVertices - 1) System.out.println("Impossible");

            else {
                System.out.println(cost);
                Collections.sort(edgePair);
                for (couple C : edgePair) {
                    System.out.println(C.first + " " + C.second);
                }
            }
        }
    }
}