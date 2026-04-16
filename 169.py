class Solution:
    def majorityElement(self, nums):
        count, candidate = 0, None
        
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        
        # Optional verification
        if nums.count(candidate) > len(nums)//2:
            return candidate
        return None
        