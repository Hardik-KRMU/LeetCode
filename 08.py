class Solution:
    def myAtoi(self, s):
        i = 0
        n = len(s)

        # 1. skip spaces
        while i < n and s[i] == ' ':
            i += 1

        # 2. sign
        sign = 1
        if i < n and (s[i] == '+' or s[i] == '-'):
            sign = -1 if s[i] == '-' else 1
            i += 1

        # 3. convert digits
        res = 0
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        while i < n and s[i].isdigit():
            digit = int(s[i])

            # 4. overflow check
            if res > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN

            res = res * 10 + digit
            i += 1

        return sign * res