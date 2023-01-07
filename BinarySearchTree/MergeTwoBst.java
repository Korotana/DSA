//Initial Template for Java

/*package whatever //do not write package name here */

import java.io.*;
import java.util.*;
import java.math.*;

class Node
{
    int data;
    Node left, right;

    public Node(int d)
    {
        data = d;
        left = right = null;
    }
}

class GFG
{
    static Node buildTree(String str)
    {
        // Corner Case
        if(str.length() == 0 || str.equals('N'))
            return null;
        String[] s = str.split(" ");

        Node root = new Node(Integer.parseInt(s[0]));
        Queue <Node> q = new LinkedList<Node>();
        q.add(root);

        // Starting from the second element
        int i = 1;
        while(!q.isEmpty() && i < s.length)
        {
              // Get and remove the front of the queue
              Node currNode = q.remove();

              // Get the curr node's value from the string
              String currVal = s[i];

              // If the left child is not null
              if(!currVal.equals("N"))
              {

                  // Create the left child for the curr node
                  currNode.left = new Node(Integer.parseInt(currVal));

                  // Push it to the queue
                  q.add(currNode.left);
              }

              // For the right child
              i++;
              if(i >= s.length)
                  break;
              currVal = s[i];

              // If the right child is not null
              if(!currVal.equals("N"))
              {

                  // Create the right child for the curr node
                  currNode.right = new Node(Integer.parseInt(currVal));

                  // Push it to the queue
                  q.add(currNode.right);
              }

              i++;
        }

        return root;
    }

    public static void main(String args[]) throws IOException {

       BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine().trim());
        while(t>0)
        {
            String s = br.readLine();
            Node root1 = buildTree(s);

            s = br.readLine();
            Node root2 = buildTree(s);

            Solution T = new Solution();
            List<Integer> ans = T.merge(root1,root2);
            for(int i=0;i<ans.size();i++)
                System.out.print(ans.get(i) + " ");
            System.out.println();

            t--;
        }
    }
}
// } Driver Code Ends


//User function Template for Java


class Solution
{

    public void ino(Node n,List<Integer> list){
        if (n== null){
            return;
        }

        ino(n.left,list);
        list.add(n.data);
        ino(n.right,list);


    }

    public List<Integer> mrg(List<Integer> list1,List<Integer> list2){
        List<Integer> li3 = new ArrayList<Integer>();
        int i = 0;
        int j = 0;

        while (i< list1.size() && j < list2.size()){
            if (list1.get(i)<list2.get(j)){
                li3.add(list1.get(i));
                i++;
            }else{
                li3.add(list2.get(j));
                j++;
            }

        }
        while (i < list1.size()){
            li3.add(list1.get(i));
            i++;
        }

        while (j < list2.size()){
            li3.add(list2.get(j));
            j++;
        }

        return li3;
    }

    // public Node tre(List<Integer> list,int strt,int end){

    //     if (strt > end){
    //         return null;
    //     }

    //     int mid = (strt+end)/2;
    //     Node node = new Node(list.get(mid));

    //     node.left = tre(list, strt, mid-1);
    //     node.right = tre(list,mid+1,end);

    //     return node;

    // }

    //Function to return a list of integers denoting the node
    //values of both the BST in a sorted order.
    public List<Integer> merge(Node root1,Node root2)
    {


        List<Integer> list1 = new ArrayList<Integer>();
        List<Integer> list2 = new ArrayList<Integer>();

        ino(root1,list1);
        ino(root2,list2);

        return mrg(list1,list2);
        // Node node = tre(list3,0,list3.size());


        // Write your code here
    }
}
