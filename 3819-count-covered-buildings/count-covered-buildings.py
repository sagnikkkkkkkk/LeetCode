class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        
        pts = set((x , y) for x , y in buildings)

        rows_min  = {}
        rows_max  = {}        
        cols_min  = {}
        cols_max  = {}

        for x , y in pts :
            if x in rows_min :
                if y < rows_min[x] :
                    rows_min[x] = y
                if y > rows_max[x] :
                    rows_max[x] = y

            else :
                rows_min[x] = rows_max[x] = y

            if y in cols_min :
                if x < cols_min[y] :
                    cols_min[y] = x
                if x > cols_max[y] :
                    cols_max[y] = x
            
            else :
                cols_min[y] = cols_max[y] = x
                
        covered = 0
        for x , y in pts :
            if rows_min[x] < y < rows_max[x] and cols_min[y] < x < cols_max[y] :
                covered += 1

        return covered