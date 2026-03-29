class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        
        e1 = sorted([s1[0] , s1[2]])
        e2 = sorted([s2[0] , s2[2]])

        o1 = sorted([s1[1] , s1[3]])
        o2 = sorted([s2[1] , s2[3]])

        return e1 == e2 and o1 == o2
        