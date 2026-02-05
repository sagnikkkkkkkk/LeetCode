class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        r = [0]*n

        for i in range(n):
            if nums[i] == 0:
                r[i] = 0
            else:
                n_i = (i + nums[i]) % n
                r[i] = nums[n_i]

        return r

            