class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        
        a = []

        for n in nums:
            if n & (n-1) == 0:
                a.append(-1)
            else:
                t = 0
                while n & (1 << t):
                    t += 1
                a.append(n ^ (1 << (t - 1)))

        return a