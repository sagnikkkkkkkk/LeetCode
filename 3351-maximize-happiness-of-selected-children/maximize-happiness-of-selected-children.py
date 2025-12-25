class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        
        happiness.sort(reverse = True)

        t = 0                                       #   t = total 

        for i in range(k) :
            c = happiness[i] - i                    #   c = current
            if c > 0 :
                t += c
            else :
                break

        return t