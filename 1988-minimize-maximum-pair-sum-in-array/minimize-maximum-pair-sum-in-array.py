class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        
        nums.sort()
        l , r = 0 , len(nums) - 1
        mps = 0

        while l < r:
            mps = max(mps , nums[l] + nums[r])
            l += 1
            r -= 1

        return mps