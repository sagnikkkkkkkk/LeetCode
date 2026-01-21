class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        
        a = []

        for p in nums:
            if p & (p - 1) == 0:
                a.append(-1)
                continue

            b = 1

            while p & b:
                b <<= 1

            a.append(p - (b >> 1))

        return a