
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        alphabet1 = {}
        alphabet2 = {}

        if (len(s)!=len(t)):
            return False


        for cnt in range(0,len(s)):
            alphabet1[s[cnt]] = alphabet1.get(s[cnt],0) + 1
            alphabet2[t[cnt]] = alphabet2.get(t[cnt],0) + 1


        if alphabet1==alphabet2:
            return True
        else:
            return False