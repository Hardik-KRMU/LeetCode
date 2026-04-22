class Solution:
    def wordPattern(self, pattern, s):
        words = s.split()
        
        if len(pattern) != len(words):
            return False
        
        a = {}
        b = {}

        for x, y in zip(pattern, words):
            if a.get(x, y) != y or b.get(y, x) != x:
                return False
            a[x] = y
            b[y] = x

        return True