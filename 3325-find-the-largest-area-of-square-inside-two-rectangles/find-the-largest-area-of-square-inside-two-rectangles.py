class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        
        n   = len(bottomLeft)
        m_a = 0

        for i in range(n):
            x1 , y1 = bottomLeft[i]
            x2 , y2 = topRight[i]

            for j in range(i+1 , n):
                x3 , y3 = bottomLeft[j]
                x4 , y4 = topRight[j]

                l = max(x1 , x3)
                r = min(x2 , x4)
                b = max(y1 , y3)
                t = min(y2 , y4)

                if l < r and b < t:
                    s   = min(r-l , t-b)
                    m_a = max(m_a , s*s)


        return m_a
