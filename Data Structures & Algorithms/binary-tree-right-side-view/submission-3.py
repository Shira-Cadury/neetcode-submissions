# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        queue = deque([root])
        while queue:
            levelSize = len(queue)
            for i in range(levelSize):
                node = queue.popleft()
                if i == levelSize - 1:
                    res.append(node.val)
                if node.left != None:    
                    queue.append(node.left)
                if node.right != None:    
                    queue.append(node.right)    
        return res                    
        