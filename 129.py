class Solution:
    def sumNumbers(self, root):
        if not root:
            return 0
        
        stack = [(root, root.val)]
        total = 0
        
        while stack:
            node, num = stack.pop()
            
            if not node.left and not node.right:
                total += num
            
            if node.left:
                stack.append((node.left, num * 10 + node.left.val))
            if node.right:
                stack.append((node.right, num * 10 + node.right.val))
        
        return total