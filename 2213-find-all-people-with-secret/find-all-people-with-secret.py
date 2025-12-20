class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        
        meetings.sort(key = lambda x: x[2])

        s = set([0 , firstPerson])                  #   s = secret
        i = 0
        m = len(meetings)

        while i < m :
            t = meetings[i][2]                      #   t  = time
            g = defaultdict(list)                   #   g  = graph
            p = set()                               #   p  = people

            while i < m and meetings[i][2] == t :   #   m
                x , y , _ = meetings[i]
                g[x].append(y)                      #   x
                g[y].append(x)                      #   y
                p.add(x)
                p.add(y)
                i += 1

            q = deque()                             #   q = queue
            v = set()                               #   v = visited

            for a in p :                            #   a
                if a in s :
                    q.append(a)
                    v.add(a)

            while q :                               #   u
                u = q.popleft()
                for b in g[u] :                     #   b
                    if b not in v :
                        v.add(b)
                        q.append(b)

            s.update(v)

        return list(s)


