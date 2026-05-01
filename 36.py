class Solution:
    def isValidSudoku(self, board):
        seen = set()

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val != '.':
                    if (val, r) in seen or (c, val) in seen or (r//3, c//3, val) in seen:
                        return False
                    seen.add((val, r))
                    seen.add((c, val))
                    seen.add((r//3, c//3, val))
        return True