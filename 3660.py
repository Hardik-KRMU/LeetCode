class Solution:
    def maxValue(self, nums):
        n = len(nums)

        # prefix maximums
        pre = [0] * n
        pre[0] = nums[0]

        for i in range(1, n):
            pre[i] = max(pre[i - 1], nums[i])

       