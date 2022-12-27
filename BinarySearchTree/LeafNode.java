package BST;//Initial Template for Java
import java.util.*;
import java.lang.*;
import java.io.*;
class GFG
{
    public static void main(String[] args) throws IOException
    {
        BufferedReader read = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(read.readLine().trim());
        while(T-->0)
        {
            int N = Integer.parseInt(read.readLine());
            String input_line[] = read.readLine().trim().split("\\s+");
            int arr[]= new int[N];
            for(int i = 0; i < N; i++)
                arr[i] = Integer.parseInt(input_line[i]);
            Solution ob = new Solution();
            int[] ans = ob.leafNodes(arr, N);
            for(int i = 0; i < ans.length; i++)
            {
                System.out.print(ans[i] + " ");
            }
            System.out.println();
        }
    }
}
// } Driver Code Ends


//User function Template for Java
class Solution
{
    // void leaf(int arr[], int N, int n[]){
    //     if (arr.get(N+1) == null && arr.get(N) < arr.get(N-1){
    //         n.add(arr.get(N));
    //     }
    // }

    public int[] leafNodes(int arr[], int N)
    {
//        int n =N/2;
        int leaf[] = new int[N/2+1];
        int x=0;
        Stack<Integer> s = new Stack<>();
        for (int i=0,j=1;j<N;i++,j++){
            boolean bool = false;
            if (arr[i] > arr[j]){
                s.push(arr[i]);
            }else {
                while (!s.isEmpty()){
                    if (arr[j] > s.peek()){
                        s.pop();
                        bool = true;
                    }else {
                        break;
                    }
                }
                if (bool){
                    leaf[x] = arr[i];
                    x++;
                }
            }
        }
        leaf[x] = arr[N-1];
        if (x==0){
            int[] temp = {leaf[0]};
            return temp;
        }
        int temp[] = new int[x+1];
        for (int k=0;k<=x;k++){
            temp[k] = leaf[k];
        }
        return temp;
    }
}