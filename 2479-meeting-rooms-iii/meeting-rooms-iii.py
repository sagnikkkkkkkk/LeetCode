class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        
        meetings.sort()

        a = list(range(n))                                      #   a = avalable
        heapq.heapify(a)

        b = []                                                  #   b = busy
        c = [0]*n                                               #   c = count
                                                                #   e = end
        for s , e in meetings :                                 #   s = start
            d = e - s                                           #   d = duration
            while b and b[0][0] <= s :
                _ , r = heapq.heappop(b)                        #   r = room
                heapq.heappush(a , r)

            if a :
                r = heapq.heappop(a)
                heapq.heappush(b , (e , r))
            else :
                ee , r = heapq.heappop(b)                       #   ee = earliest_end
                heapq.heappush(b , (ee + d , r))

            c[r] += 1

        return c.index(max(c))