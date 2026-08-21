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

class Solution {
    private HashMap<Integer, Integer> map=new HashMap<>();
    private int p=0;
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        for(int i=0; i<inorder.length; i++)
        {
            map.put(inorder[i],i);
        }
        return build(preorder,0,inorder.length-1);
    }

    private TreeNode build(int[] pre,int left,int right)
    {
        if(left > right)
            return null;
        int v=pre[p++];    
        TreeNode n=new TreeNode(v);
        int m=map.get(v);
        n.left= build(pre,left, m-1);
        n.right=build(pre,m+1, right);    
        return n;
    }
}
