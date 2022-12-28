package Kattis;

import java.io.*;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.*;

//import java.util.*;
//
//class GFG
//{
//    static int N = 100000;
//
//    // To keep correct and reverse direction
//    @SuppressWarnings("unchecked")
//    static Vector<Integer>[] gr1 = new Vector[N];
//    @SuppressWarnings("unchecked")
//    static Vector<Integer>[] gr2 = new Vector[N];
//
//    static boolean[] vis1 = new boolean[N];
//    static boolean[] vis2 = new boolean[N];
//
//    static {
//        for (int i = 0; i < N; i++)
//        {
//            gr1[i] = new Vector<>();
//            gr2[i] = new Vector<>();
//        }
//    }
//
//    // Function to add edges
//    static void Add_edge(int u, int v)
//    {
//        gr1[u].add(v);
//        gr2[v].add(u);
//    }
//
//    // DFS function
//    static void dfs1(int x)
//    {
//        vis1[x] = true;
//        for (int i : gr1[x])
//            if (!vis1[i])
//                dfs1(i);
//    }
//
//    // DFS function
//    static void dfs2(int x)
//    {
//        vis2[x] = true;
//        for (int i : gr2[x])
//            if (!vis2[i])
//                dfs2(i);
//    }
//
//    static boolean Is_connected(int n)
//    {
//
//        // Call for correct direction
//        Arrays.fill(vis1, false);
//        dfs1(1);
//
//        // Call for reverse direction
//        Arrays.fill(vis2, false);
//        dfs2(1);
//
//        for (int i = 1; i <= n; i++)
//        {
//
//            // If any vertex it not visited in any direction
//            // Then graph is not connected
//            if (!vis1[i] && !vis2[i])
//                return false;
//        }
//
//        // If graph is connected
//        return true;
//    }
//
//    // Driver Code
//    public static void main(String[] args)
//    {
//        int n = 4;
//
//        // Add edges
//        Add_edge(1, 2);
//        Add_edge(1, 3);
//        Add_edge(2, 3);
//        Add_edge(3, 4);
//
//        // Function call
//        if (Is_connected(n))
//            System.out.println("Yes");
//        else
//            System.out.println("No");
//    }
//}
//
//
//class WheresmyInternet {
//
//    static void dfs(int src,HashMap<Integer,HashSet<Integer>> map,boolean[] vis){
//        vis[src] = true;
//        for (Integer i : map.get(src)){
//            if (!vis[i]){
//                dfs(i,map,vis);
//            }
//        }
//    }
//
//    public static void main(String[] args) {
//        Scanner sc = new Scanner(System.in);
//
//        int houses = sc.nextInt();
//        int cables = sc.nextInt();
//
//        int x, y, z = 0;
//
//        HashMap<Integer,HashSet<Integer>> Map = new HashMap<>();
//        for (int i = 0; i <= houses; i++) {
//            Map.put(i , new HashSet<>());
//        }
//
//        boolean[] vis = new boolean[houses+1];
//
//        for (int i = 0; i < cables; i++) {
//            x = sc.nextInt();
//            y = sc.nextInt();
//            Map.get(x).add(y);
//            Map.get(y).add(x);
//        }
//
//        dfs(1,Map,vis);
//
//        for (int i = 1; i < houses; i++) {
//            if (!vis[i]){
//                z = 1;
//                break;
//            }
//        }
//
//
//        if (z != 0){
//            for (int i = 1; i <= houses ; i++) {
//                if (!vis[i]){
//                    System.out.println(i);
//                }
//            }
//        }else {
//            System.out.println("Connected");
//        }
//    sc.close();
//    }
//}

class knapsack {

   public static void main(String[] args) throws Exception {
       BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
       PrintWriter out = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));

       String line = "";
       while ((line = in.readLine()) != null) {
           StringTokenizer st = new StringTokenizer(line);
           int c = Integer.parseInt(st.nextToken());
           int n = Integer.parseInt(st.nextToken());
           int[] wt = new int[n];
           int[] v = new int[n];
           for (int i = 0; i < n; i++) {
               st = new StringTokenizer(in.readLine());
               v[i] = Integer.parseInt(st.nextToken());
               wt[i] = Integer.parseInt(st.nextToken());
           }
           int[][] dp = new int[n + 1][c + 1];
           for (int i = 0; i < dp.length; i++)
               Arrays.fill(dp[i], -1);
           for (int i = 0; i <= n; i++) {
               for (int w = 0; w <= c; w++) {
                   if (i == 0 || w == 0)
                       dp[i][w] = 0;
                   else if (wt[i - 1] <= w)
                       dp[i][w] = Math.max(dp[i - 1][w], v[i - 1] + dp[i - 1][w - wt[i - 1]]);
                   else
                       dp[i][w] = dp[i - 1][w];
               }
           }
//            out.println(dp[n - 1][c]);
           int temp = c;
           ArrayList<Integer> indices = new ArrayList<Integer>();
           for(int i = n; i > 0; i--) {
               if(dp[i][temp] != dp[i - 1][temp]) {
                   indices.add(i - 1);
                   temp -= wt[i - 1];
               }

           }
           out.println(indices.size());
           for(int i : indices)
               out.print(i + " ");
           out.println();
       }
       out.close();
   }
}