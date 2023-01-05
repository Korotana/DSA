import java.util.*;
import java.lang.*;
import java.io.*;

class Main{
	public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int t = sc.nextInt();

        for (int i = 0; i < t; i++) {
            int n = sc.nextInt();
            int s = sc.nextInt();

            int[] m = new int[n];
            for (int j = 0; j < n; j++) {
                m[j] = sc.nextInt();
            }

            Solution obj = new Solution();
            ArrayList<Integer> res = obj.subarraySum(m, n, s);
            for(int ii = 0;ii<res.size();ii++)
                System.out.print(res.get(ii) + " ");
            System.out.println();
        }
    }

}// } Driver Code Ends


class Solution
{
    //Function to find a continuous sub-array which adds up to a given number.
    static ArrayList<Integer> subarraySum(int[] arr, int n, int s)
    {
        int l = 0;
        int sum = arr[0];
        ArrayList<Integer> subarr = new ArrayList();

        for (int i = 1; i <= n ; i++){
            // sum = arr[i];
            while (sum > s && l < i-1){
                sum -= arr[l];
                l++;
            }
            if (sum == s){
                subarr.add(l+1);
                subarr.add(i);
                return subarr;
                // break;
            }
            if (i < n){
            sum += arr[i];}
            // if (i == n && (sum + arr[i-1] != s) ){
            //     subarr.add(-1);
            //     return subarr;
            // }
        }
        subarr.add(-1);
        return subarr;
        // Your code here
    }
}