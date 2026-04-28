class Solution:
    def firstUniqChar(self, s):
         freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1