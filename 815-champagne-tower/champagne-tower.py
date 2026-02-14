class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        
        a = [0.0] * (query_row + 2)
        a[0] = poured

        for i in range(query_row):
            b = [0.0] * (query_row + 2)
            for j in range(i+1):
                x = max(0.0 , a[j] - 1) / 2
                b[j] += x
                b[j+1] += x
            a = b
        return min(1.0 , a[query_glass])