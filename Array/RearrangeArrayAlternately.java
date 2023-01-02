import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
	public static void main (String[] args)throws IOException
	{

// 		Scanner in = new Scanner(System.in);

// 		int t = in.nextInt();
        BufferedReader read = new BufferedReader(new InputStreamReader(System.in));

         //testcases
        int t = Integer.parseInt(read.readLine());

		while(t-- >0)
		{
		    //size of array
		    int n = Integer.parseInt(read.readLine());
		    int[] temp= new int[n];

		    String str[] = read.readLine().trim().split(" ");

		    //adding elements to the array
		    for(int i=0;i<n;i++)
		        temp[i] = Integer.parseInt(str[i]);

		    // StringBuffer sb = new StringBuffer();

		    Solution ob = new Solution();

		    //calling rearrange() function
		    ob.rearrange(temp, n);
		    StringBuffer sb = new StringBuffer();

		    //appending and printing the elements
		    for(int i =0; i < n; i++)
		     sb.append(temp[i] + " ");
		    System.out.println(sb);
		}
	}
}



// } Driver Code Ends


class Solution{

    // temp: input array
    // n: size of array
    //Function to rearrange  the array elements alternately.
    public static void rearrange(int arr[], int n){

        int a[] = arr.clone();

        int max = n-1;
        int min = 0;

        boolean swap=true;
        for (int i = 0; i < n;i++){
            if (swap){
                arr[i]=a[max--];
            }else{
                arr[i]=a[min++];
            }
            swap=!swap;

        }
        // Your code here

    }

}

