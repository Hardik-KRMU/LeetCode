cclass Solution:
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
