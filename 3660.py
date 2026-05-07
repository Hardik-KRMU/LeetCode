class Solution:
    def maxValue(self, nums):
        n = len(nums)

        # prefix maximums
        pre = [0] * n
        pre[0] = nums[0]

        for i in range(1, n):
            pre[i] = max(pre[i - 1], nums[i])

        ans = [0] * n
        ans[-1] = pre[-1]

        suf_min = nums[-1]

        # process from right to left
        for i in range(n - 2, -1, -1):

            # if we can connect with the right side
            if pre[i] > suf_min:
                ans[i] = ans[i + 1]
            else:
                ans[i] = pre[i]

            suf_min = min(suf_min, nums[i])

        return ans