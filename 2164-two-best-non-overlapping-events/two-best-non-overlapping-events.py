class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        
        events.sort(key = lambda  x : x[0])
        n = len(events)

        sm = [0] * (n + 1)                                  # sm = suf_max
        for i in range(n-1 , -1 , -1) :
            sm[i] = max(sm[i + 1] , events[i][2])

        st = [event[0] for event in events]                 # st = starts
        ans = 0

        for i in range(n) :
            s , e , v = events[i]                           #   s  = start
            
            l , r = 0 ,n                                    #   e  = end
            while l < r :                                   #   v  = value
                m = (l + r) // 2                            #   m = mid
                if st[m] <= e :
                    l = m + 1                               #   l = left  
                else :
                    r = m
                                                            #   r = right
            j = l                                           #   br = bisect right
            ans = max(ans , v + sm[j])                      #   st = starts
                                                            #   e  = end
        

        return ans
