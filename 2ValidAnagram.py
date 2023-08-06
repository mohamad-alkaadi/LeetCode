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
