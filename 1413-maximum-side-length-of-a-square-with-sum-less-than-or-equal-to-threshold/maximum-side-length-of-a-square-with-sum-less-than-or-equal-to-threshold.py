class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        
        r , c = len(mat) , len(mat[0])

        ps = [[0] * (c+1) for _ in range(r+1)]

        for i in range(1 , r+1):
            for j in range(1 , c+1):
                ps[i][j] = (
                    mat[i - 1][j - 1]
                    + ps[i - 1][j]
                    + ps[i][j-1]
                    - ps[i - 1][j - 1]
                )

        def ok(k):
            for i in range(r - k +1):
                for j in range(c - k + 1):
                    s = (
                        ps[i + k][j + k]
                        - ps[i][j + k]
                        - ps[i + k][j]
                        + ps[i][j]
                    )
                    if s <= threshold:
                        return True
            return False

        l , h = 0 , min(r,c)
        ans = 0

        while l <= h:
            m = (l + h) // 2
            if ok(m):
                ans = m
                l = m + 1
            else:
                h = m - 1
        
        return ans
        
            