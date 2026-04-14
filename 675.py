from collections import deque

class Solution:
    def cutOffTree(self, forest):
        m, n = len(forest), len(forest[0])
        
        # Step 1: collect trees
        trees = [(forest[i][j], i, j)
                 for i in range(m)
                 for j in range(n)
                 if forest[i][j] > 1]
        
        trees.sort()
        
        # BFS function
        def bfs(sr, sc, tr, tc):
            if sr == tr and sc == tc:
                return 0
            
            visited = [[False]*n for _ in range(m)]
            queue = deque([(sr, sc, 0)])
            visited[sr][sc] = True
            
            while queue:
                r, c, d = queue.popleft()
                
                for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                    nr, nc = r+dr, c+dc
                    
                    if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc] and forest[nr][nc] != 0:
                        if nr == tr and nc == tc:
                            return d + 1
                        
                        visited[nr][nc] = True
                        queue.append((nr, nc, d+1))
            
            return -1
        
        # Step 2: process trees
        sr = sc = 0
        steps = 0
        
        for _, tr, tc in trees:
            dist = bfs(sr, sc, tr, tc)
            if dist == -1:
                return -1
            
            steps += dist
            sr, sc = tr, tc
        
        return steps