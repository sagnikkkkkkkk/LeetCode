class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        
        r , c = len(grid) , len(grid[0])                    #   r  = rows
        ct = 0                                              #   c  = cols
                                                            #   ct = count

        def im(x , y):                                      #   im = is_magic
            if grid[x+1][y+1] != 5 :
                return False

            seen = set()
            for i in range(x , x+3):
                for j in range(y , y+3):
                    v = grid[i][j]                          #   v = val
                    if v < 1 or v > 9 :
                        return False
                    seen.add(v)

            if len(seen) != 9 :
                return False 

            for i in range(3):                                 #   x = r
                if sum(grid[x+i][y : y+3]) != 15 :              #   y = c
                    return False

            for j in range(3):
                if grid[x][y+j] + grid[x+1][y+j] + grid[x+2][y+j] != 15:
                    return False

            if grid[x][y] + grid[x+1][y+1] + grid[x+2][y+2] != 15:
                return False
            
            if grid[x][y+2] + grid[x+1][y+1] + grid[x+2][y] != 15:
                return False

            return True

        for i in range(r - 2):
            for j in range(c - 2):
                if im(i , j):
                    ct += 1

        return ct