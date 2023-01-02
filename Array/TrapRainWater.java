import java.io.*;
import java.util.*;
import java.lang.*;


class Array {

	public static void main (String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.parseInt(br.readLine().trim()); //Inputting the testcases
		while(t-->0){

		    //size of array
		    int n = Integer.parseInt(br.readLine().trim());
		    int arr[] = new int[n];
		    String inputLine[] = br.readLine().trim().split(" ");

		    //adding elements to the array
		    for(int i=0; i<n; i++){
		        arr[i] = Integer.parseInt(inputLine[i]);
		    }

		    Solution obj = new Solution();

		    //calling trappingWater() function
		    System.out.println(obj.trappingWater(arr, n));
		}
	}
}

// } Driver Code Ends



class Solution{

    // arr: input array
    // n: size of array
    // Function to find the trapped water between the blocks.
    static int trappingWater(int arr[], int n) {

        int watr = 0;
        int extra = 0;
        int leftindx = 0;
        int left = arr[0];
        for (int i = 1; i <= n-1; i++) {
            if (arr[i] < left){
                watr +=left - arr[i];
                extra +=left - arr[i];
            }else {
                leftindx = i;
                left = arr[i];
                extra = 0;
            }
        }
        if (leftindx < n-1){
            watr -= extra;
            left = arr[n-1];
            for (int i = n-1; i >= leftindx; i--) {
                if (arr[i] >= left){
                    left = arr[i];
                }else {
                    watr += left - arr[i];
                }
            }
        }

        return watr;
    }
}

