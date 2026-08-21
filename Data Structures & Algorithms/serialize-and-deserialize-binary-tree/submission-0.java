/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

public class Codec {

    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        StringBuilder sb = new StringBuilder();
        DFS(root, sb);
        String ans=sb.toString();
        return ans;
    }

    private void DFS(TreeNode node, StringBuilder sb)
    {
        if(node == null)
        {
          sb.append("null").append(",");
          return;
        }
            
        sb.append(node.val).append(",");
        DFS(node.left, sb);
        DFS(node.right, sb);   
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        String[] values = data.split(",");
        Queue<String> queue = new LinkedList<>(Arrays.asList(values));
        TreeNode root=help(queue);
        return root;
    }

    private TreeNode help(Queue<String> q)
    {
        if(q ==null || q.isEmpty())
            return null;
        String v = q.poll(); 
        if(v.equals("null"))   
            return null;
        TreeNode node= new TreeNode();
        node.val=Integer.parseInt(v);
        node.left=help(q);
        node.right=help(q);    
        return node;
    }
}
