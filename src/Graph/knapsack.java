//package Kattis;
//
//
//import java.io.*;
//import java.util.*;
//
//class knapsack {
//    int capacity ;
//    int numItems ;
//    HashMap<Integer, HashSet<Integer>> Map;
//
////    static void calcknapsack(int[] values,int[] weight,int numItems,int capacity) {
////
////
////        PrintWriter out = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
////        int[][] dp = new int[numItems+1][capacity+1];
////        for (int i = 0; i <=numItems ; i++) {
////            for (int j = 0; j <= capacity ; j++) {
////                if (i == 0 || j == 0){
////                    dp[i][j] = 0;
////                }
////                else if (weight[i-1] > j){
////                    dp[i][j] = dp[i-1][j];
////                }else {
////                    dp[i][j] = Math.max(values[i-1] + dp[i-1][j-weight[i-1]],dp[i-1][j]);
////                }
////            }
////        }
////        ArrayList<Integer> output = new ArrayList<>();
////        int i = numItems, j = capacity;
////        while (i > 0 && j > 0){
////            if (dp[i][j] != dp[i-1][j-1]){
////                output.add(i-1);
////                i--;
////                j = j - weight[i];
////            }else {
////                i--;
////            }
////        }
////        out.println(output.size());
//////        System.out.println(output.size());
////        for (int k = 0; k < output.size(); k++) {
//////            System.out.print(output.get(k));
////            out.print(output.get(k));
////        }
////        out.println();
////        out.c
////    }
//
//
//    public static void main(String[] args) throws Exception {
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        PrintWriter pr = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
//
//        String line = "";
//        while ((line = br.readLine()) != null) {
//            StringTokenizer token = new StringTokenizer(line);
//
//            int capacity = Integer.parseInt(token.nextToken());
//            int numItems = Integer.parseInt(token.nextToken());
//
//            int[] weight = new int[numItems];
//            int[] values = new int[numItems];
//
//            for (int i = 0; i < numItems; i++) {
//                token = new StringTokenizer(br.readLine());
//                values[i] = Integer.parseInt(token.nextToken());
//                weight[i] = Integer.parseInt(token.nextToken());
//            }
//
//
//            int[][] dp = new int[numItems + 1][capacity + 1];
////            for (int i = 0; i < dp.length; i++)
////                Arrays.fill(dp[i], -1);
//            for (int i = 0; i <= numItems; i++) {
//                for (int j = 0; j <= capacity; j++) {
//                    if (i == 0 || j == 0)
//                        dp[i][j] = 0;
//                    else if (weight[i - 1] <= j)
//                        dp[i][j] = Math.max(dp[i - 1][j], values[i - 1] + dp[i - 1][j - weight[i - 1]]);
//                    else
//                        dp[i][j] = dp[i - 1][j];
//                }
//            }
//
//            ArrayList<Integer> output = new ArrayList<Integer>();
//
//            int cap = capacity;
//            for(int i = numItems; i > 0; i--) {
//                if(dp[i][cap] != dp[i - 1][cap]) {
//                    output.add(i - 1);
//                    cap -= weight[i - 1];
//                }
//            }
//
//            pr.println(output.size());
//            for(int i : output)
//                pr.print(i + " ");
//            pr.println();
//        }
//        pr.close();
//    }
//}
//
