class Solution:
    def bestClosingTime(self, customers: str) -> int:

        p = customers.count('Y')                    #   p  = penalty
        mp = p  
        bh = 0                                      #   mp = min penalty
                                                    #   bh = best hour

        for i , c in enumerate(customers) :
            if c == 'Y' :
                p -= 1
            else :
                p += 1

            if p < mp :
                mp = p
                bh = i + 1                          

        return bh