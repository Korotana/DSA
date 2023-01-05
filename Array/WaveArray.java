import java.io.*;
import java.util.*;

class GFG {

	public static void main (String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.parseInt(br.readLine().trim()); //Inputting the testcases

		while(t-->0)
		{
		    int n = Integer.parseInt(br.readLine().trim());// taking size of array
		    int arr[] = new int[n]; // declaring array of size n
		    String inputLine[] = br.readLine().trim().split(" ");
		    for(int i=0; i<n; i++){
		        arr[i]=Integer.parseInt(inputLine[i]); // input elements of array
		    }

		    Solution obj = new Solution();


		    obj.convertToWave(arr, n);

		    StringBuffer sb = new StringBuffer();
            for (int i = 0; i < n; i++)
                sb.append(arr[i] + " ");

		    System.out.println(sb); // print array
		}
	}
}


 // } Driver Code Ends
class Solution{


    // arr: input array
    // n: size of the array
    //Function to sort the array into a wave-like array.
    public static void convertToWave(int arr[], int n){
        for (int i = 0; i < n-1; i++) {
            int one = arr[i];
            int two = arr[i+1];
            if (one < two & i%2==0){
                int x = one;
                arr[i] = two;
                arr[i+1] = x;
            }
        }
        // Your code here

    }

}
