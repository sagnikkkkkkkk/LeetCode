class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        
        ta = sum(apple)                         #   ta = total apples

        capacity.sort(reverse = True)

        cc = 0                                  #   cc = current capacity
        bu = 0                                  #   bu = boxes used

        for c in capacity :                     #   c  = cap
            cc += c
            bu += 1 

            if cc >= ta :
                return bu