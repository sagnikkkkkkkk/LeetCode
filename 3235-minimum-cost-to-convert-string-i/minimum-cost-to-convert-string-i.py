class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        
        I = 10**18
        d = [[I]*26 for _ in range(26)]
        for i in range(26):
            d[i][i] = 0
        for a,b,c in zip(original , changed , cost):
            d[ord(a) - 97][ord(b) - 97] = min(d[ord(a) - 97][ord(b) - 97] , c)
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    d[i][j] = min(d[i][j] , d[i][k] + d[k][j])
        r = 0 
        for a,b in zip(source , target):
            if a != b :
                x,y = ord(a) - 97 , ord(b) - 97
                if d[x][y] == I:
                    return -1
                r += d[x][y]
        return r