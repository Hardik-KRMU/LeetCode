class Solution:
    def isIsomorphic(self, s, t):
        a = {}
        b = {}

        for x, y in zip(s, t):
            if a.get(x, y) != y or b.get(y, x) != x:
                return False
            a[x] = y
            b[y] = x

        return True
        