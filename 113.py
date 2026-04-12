class Solution:
    def pathSum(self, root, s):
        res = []
        
        def dfs(node, s, path):
            if not node: return
            
            path.append(node.val)
            
            if not node.left and not node.right and node.val == s:
                res.append(path[:])
            else:
                dfs(node.left, s - node.val, path)
                dfs(node.right, s - node.val, path)
            
            path.pop()
        
        dfs(root, s, [])
        return res