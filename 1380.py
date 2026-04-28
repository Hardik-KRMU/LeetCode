<<<<<<< HEAD
class Solution:
    def luckyNumbers(self, matrix):
        rows = {min(row) for row in matrix}
        cols = {max(col) for col in zip(*matrix)}
=======
class Solution:
    def luckyNumbers(self, matrix):
        rows = {min(row) for row in matrix}
        cols = {max(col) for col in zip(*matrix)}
>>>>>>> 0120bca (first commit)
        return list(rows & cols)