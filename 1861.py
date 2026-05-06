class Solution:
    def rotateTheBox(self, box):
        m, n = len(box), len(box[0])

        # apply gravity (move stones right)
        for r in range(m):
            empty = n - 1
            for c in range(n - 1, -1, -1):
                if box[r][c] == '*':
                    empty = c - 1
                elif box[r][c] == '#':
                    box[r][c] = '.'
                    box[r][empty] = '#'
                    empty -= 1

        # rotate 90° clockwise
        res = [[0] * m for _ in range(n)]
        for r in range(m):
            for c in range(n):
                res[c][m - 1 - r] = box[r][c]

        return res