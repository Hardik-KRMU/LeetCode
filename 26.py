class Solution:
    def removeDuplicates(self, nums):
        k = 0
        for n in nums:
            if k == 0 or n != nums[k-1]:
                nums[k] = n
                k += 1
        return k