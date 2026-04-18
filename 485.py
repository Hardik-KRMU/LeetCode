class Solution:
    def findMaxConsecutiveOnes(self, nums):
        c = m = 0
        for n in nums:
            c = c + 1 if n else 0
            m = max(m, c)
        return m