import java.util.*;

class Solution
{
    //Function to find the smallest positive number missing from the array.
    static int missingNumber(int arr[], int size)
    {

    for(int i = 0; i < size; i++)
    {


      while (arr[i] >= 1 && arr[i] <= size && arr[i] != arr[arr[i] - 1]) {

        int temp=arr[arr[i]-1];
            arr[arr[i]-1]=arr[i];
            arr[i]=temp;
      }
    }

    // Finding which index has value less than n
    for(int i = 0; i < size; i++)
        if (arr[i] != i + 1)
            return (i + 1);

    // If array has values from 1 to n
    return (size + 1);
    }
}


// { Driver Code Starts.

class Main
{
    public static void main (String[] args)
    {

		Scanner sc=new Scanner(System.in);

        //taking testcases
		int t=sc.nextInt();
		while(t-->0){

		    //input number n
			int n=sc.nextInt();
			int[] arr=new int[n];

			//adding elements to the array
			for(int i=0;i<n;i++)
				arr[i]=sc.nextInt();

			Solution obj = new Solution();

			//calling missingNumber()
			int missing = obj.missingNumber(arr,n);
			System.out.println(missing);
		}
    }
}
