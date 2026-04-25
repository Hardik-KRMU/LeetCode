class Solution:
    def transpose(self, matrix):
        rows, cols = len(matrix), len(matrix[0])
        ans = [[0] * rows for _ in range(cols)]

        for i in range(rows):
            row = matrix[i]
            for j in range(cols):
                ans[j][i] = row[j]

        return ans