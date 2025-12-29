class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        
        mp = {}
        for a in allowed:                          
            k = (a[0] , a[1])                   #   k   = key
            if k not in mp:
                mp[k] = []
            mp[k].append(a[2])

        def dfs(row):
            if len(row) == 1:
                return True

            def bt(i , p):                      #   bt = backtrack
                if i == len(row) - 1:           #   p  = path
                    return dfs("".join(p))

                r = (row[i] , row[i+1])         #   r = pair
                if r not in mp:
                    return False

                for ch in mp[r]:
                    p.append(ch)
                    if bt(i+1 , p):
                        return True
                    p.pop()
                
                return False

            return bt(0 , [])

        return dfs(bottom)