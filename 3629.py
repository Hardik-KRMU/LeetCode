from collections import defaultdict, deque

class Solution:
    def minJumps(self, nums):
        n = len(nums)

        # check prime
        def is_prime(x):
            if x < 2:
                return False
