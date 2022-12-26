package BST;

import java.util.LinkedList;
import java.util.Queue;
import java.io.*;

class DeleteNode{
    int data;
    DeleteNode left;
    DeleteNode right;
    DeleteNode(int data){
        this.data = data;
        left=null;
        right=null;
    }
}

class DeleteBstNode
{

    static DeleteNode buildTree(String str){

        if(str.length()==0 || str.charAt(0)=='N'){
            return null;
        }

        String ip[] = str.split(" ");
        // Create the root of the tree
        DeleteNode root = new DeleteNode(Integer.parseInt(ip[0]));
        // Push the root to the queue

        Queue<DeleteNode> queue = new LinkedList<>();

        queue.add(root);
        // Starting from the second element

        int i = 1;
        while(queue.size()>0 && i < ip.length) {

            // Get and remove the front of the queue
            DeleteNode currNode = queue.peek();
            queue.remove();

            // Get the current node's value from the string
            String currVal = ip[i];

            // If the left child is not null
            if(!currVal.equals("N")) {

                // Create the left child for the current node
                currNode.left = new DeleteNode(Integer.parseInt(currVal));
                // Push it to the queue
                queue.add(currNode.left);
            }

            // For the right child
            i++;
            if(i >= ip.length)
                break;

            currVal = ip[i];

            // If the right child is not null
            if(!currVal.equals("N")) {

                // Create the right child for the current node
                currNode.right = new DeleteNode(Integer.parseInt(currVal));

                // Push it to the queue
                queue.add(currNode.right);
            }
            i++;
        }

        return root;
    }
    static void printInorder(DeleteNode root)
    {
        if(root == null)
            return;

        printInorder(root.left);
        System.out.print(root.data+" ");

        printInorder(root.right);
    }

    public static void main (String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int t=Integer.parseInt(br.readLine());
        while(t > 0){
            String s = br.readLine();
            int x = Integer.parseInt(br.readLine());
            DeleteNode root = buildTree(s);
            DeleteTree g = new DeleteTree();
            root = g.deleteNode(root,x);
            printInorder(root);
            System.out.println();
            t--;

        }
    }

}

// } Driver Code Ends
//User function Template for Java


class DeleteTree
{
    static DeleteNode succ(DeleteNode n){
        DeleteNode curr = n.right;
        while(curr != null && curr.left != null ){
            curr = curr.left;
        }
        return curr;

    }

    //Function to delete a node from BST.
    public static DeleteNode deleteNode(DeleteNode root, int x)
    {

        if (root == null) {
            return null;
        }else if (root.data > x){
            root.left = deleteNode(root.left,x);
        }else if (root.data < x){
            root.right = deleteNode(root.right,x);
        }else{
            if (root.left == null) return root.right;
            else if (root.right == null) return root.left;
            else{
                DeleteNode suc = succ(root);
                root.data = suc.data;
                root.right = deleteNode(root.right,suc.data);
            }
        }
        return root;




        // code here.
    }
}