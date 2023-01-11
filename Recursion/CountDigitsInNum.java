
//User function Template for Java

class Solution
{
    // complete the below function
    public static int countDigits(int n)
    {
       if(n == 0) return 1;
    if(n < 10) return 1;
    return countDigits(n/10) + 1;}
}
