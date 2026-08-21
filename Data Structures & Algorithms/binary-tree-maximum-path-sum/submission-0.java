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
    private int max = Integer.MIN_VALUE;
    public int maxPathSum(TreeNode root) {
        maxHelp(root);
        return max;
    }

    private int maxHelp(TreeNode node)
    {
        if(node == null)
            return 0;
        int left=Math.max(maxHelp(node.left), 0);
        int right=Math.max(maxHelp(node.right), 0);
        max=Math.max(max, node.val+left+right);
        return node.val+Math.max(left, right);
    }
}
