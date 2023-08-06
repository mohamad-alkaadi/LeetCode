# my solution
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        string1 = list(s)
        string2 = list(t)
        x = len(string1)
        if len(string1) != len(string2):
            return False
        for i in range(x):
            if string2[i] not in string1:
                return False
            string1.remove(string2[i])
        return True


# learned solution 
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#            return 0
#         string1, string2 = {}, {}

#         for i in range(len(s)):
#             string1[s[i]] = 1+ string1.get(s[i], 0)
#             string2[t[i]] = 1+ string2.get(t[i], 0)
#         return string1 == string2