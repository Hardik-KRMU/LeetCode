class Solution:
    def reverseVowels(self, s):
        arr = list(s)
        v = set("aeiouAEIOU")
        l, r = 0, len(arr) - 1

        while l < r:
            while l < r and arr[l] not in v:
                l += 1
            while l < r and arr[r] not in v:
                r -= 1

            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1

        return ''.join(arr)