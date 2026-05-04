class Solution:
    def reverse(self, x):
        sign = -1 if x < 0 else 1
        s = str(abs(x))[::-1]
        res = sign * int(s)

        return res if -2**31 <= res <= 2**31 - 1 else 0