class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        freq = {}
        count = 0
        for n in nums:
            if n in freq:
                count += freq[n]
                freq[n] += 1
            else:
                freq[n] = 1
        return count 