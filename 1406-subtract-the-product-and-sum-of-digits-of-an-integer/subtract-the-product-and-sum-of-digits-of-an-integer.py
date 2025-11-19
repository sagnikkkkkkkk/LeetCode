class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        total = 0
        for d in str(n) :
            product *= int(d)
            total += int(d)
        return product - total