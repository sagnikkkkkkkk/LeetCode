class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        
        n = len(nums)
        a = float('inf')

        for i in range(1 , n-1):
            for j in range(i+1 , n):
                a = min(a , nums[0] + nums[i] + nums[j])

        return a