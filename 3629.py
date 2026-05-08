from collections import defaultdict, deque

class Solution:
    def minJumps(self, nums):
        n = len(nums)

        # check prime
        def is_prime(x):
            if x < 2:
                return False
            i = 2
            while i * i <= x:
                if x % i == 0:
                    return False
                i += 1
            return True

        # map: prime -> indices divisible by prime
        div = defaultdict(list)

        for i, num in enumerate(nums):
            x = num
            d = 2

            while d * d <= x:
                if x % d == 0:
                    div[d].append(i)
                    while x % d == 0:
                        x //= d
                d += 1
