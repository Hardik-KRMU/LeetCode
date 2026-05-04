class Solution:
    def myAtoi(self, s):
        s = s.strip()
        if not s:
            return 0

        sign = 1
        i = 0

        if s[0] in '+-':
            sign = -1 if s[0] == '-' else 1
            i += 1

        res = 0
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        while i < len(s) and s[i].isdigit():
            res = res * 10 + int(s[i])

            if sign * res >= INT_MAX:
                return INT_MAX
            if sign * res <= INT_MIN:
                return INT_MIN

            i += 1

        return sign * res