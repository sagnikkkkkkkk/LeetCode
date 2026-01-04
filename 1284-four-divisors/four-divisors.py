class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        
        def ip(x):                      #   ip = is prime
            if x < 2:
                return False
            for i in range(2 , int(x**0.5) + 1):
                if x % i == 0:
                    return False 
            return True

        t = 0                           #   t = total

        for n in nums:
            p = round(n**(1/3))
            if p**3 == n and ip(p):
                t += 1 + p + p*p + n
                continue

            for d in range(2 , int(n**0.5) + 1):
                if n % d == 0:
                    o = n // d                  #   o = other
                    if d != o and ip(d) and ip(o):
                        t += 1 + d + o + n
                    break

        return t