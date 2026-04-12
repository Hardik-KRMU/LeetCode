from collections import deque

class Solution:
    def hasPathSum(self, root, targetSum):
        if not root:
            return False
        
        queue = deque([(root, root.val)])
        
        while queue:
            node, curr_sum = queue.popleft()
            
            # Check leaf
            if not node.left and not node.right:
                if curr_sum == targetSum:
                    return True
            
            if node.left:
                queue.append((node.left, curr_sum + node.left.val))
            if node.right:
                queue.append((node.right, curr_sum + node.right.val))
        
        return False