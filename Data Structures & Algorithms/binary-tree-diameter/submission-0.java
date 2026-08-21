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
    private int maxDiameter;
    public int diameterOfBinaryTree(TreeNode root) {
        height(root);
        return maxDiameter;
    }

   private int height(TreeNode root)
   {
        if(root == null)
          return 0;

        int left=height(root.left);
        int right=height(root.right);

        if(left+right > maxDiameter)
           maxDiameter=left + right;

        if(right > left) 
          return right+1;
         else
          return left+1; 
   } 
}
