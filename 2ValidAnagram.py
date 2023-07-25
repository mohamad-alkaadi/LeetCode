class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        z = 0
        for x in s:
            for y in t:
                if y in x:
                    z = 1
                else:
                    z = 0
        if z == 0:
            return False
        elif z == 1:
            return True


    #     class Solution:
    # def isAnagram(self, s: str, t: str) -> bool:
    #     exSet = set()
    #     z = 0
        
    #     for x in s:
    #         exSet.add(x)
    #         for y in t:
    #             if y in exSet:
    #                 z = 1
    #             else:
    #                 z = 0
    #     if z == 0:
    #         return False
    #     elif z == 1:
    #         return True