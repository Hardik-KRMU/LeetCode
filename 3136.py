class Solution:
    def isValid(self, word):
        if len(word) < 3:
            return False

        v = set("aeiouAEIOU")
        a = b = False

        for ch in word:
            if not ch.isalnum():
                return False
            if ch.isalpha():
                if ch in v:
                    a = True
                else:
                    b = True

        return a and b