class Solution:
    def reverse(self, x):
        res = 0
        sign = -1 if x < 0 else 1
        x = abs(x)

        while x:
            digit = x % 10
            x //= 10

            # overflow check (32-bit)
            if res > (2**31 - 1) // 10:
                return 0

            res = res * 10 + digit

        return sign * res