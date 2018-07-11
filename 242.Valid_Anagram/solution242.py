class Solution:
    def anagram(self, s, t):
        if len(s)==len(t):
            a=list(s)
            b=list(t)
            a.sort()
            b.sort()
            if a==b:
                return True
        return False
