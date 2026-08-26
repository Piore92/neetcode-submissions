from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        alphabet1 = defaultdict(int)
        alphabet2 = defaultdict(int)

        if (len(s)!=len(t)):
            return False


        for cnt in range(0,len(s)):
            alphabet1[s[cnt]] += 1
            alphabet2[t[cnt]] += 1


        if alphabet1==alphabet2:
            return True
        else:
            return False