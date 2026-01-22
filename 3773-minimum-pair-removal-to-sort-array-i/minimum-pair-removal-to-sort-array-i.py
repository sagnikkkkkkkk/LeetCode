class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        
        c = 0

        while True:
            ok = True
            i = 1
            while i < len(nums):
                if nums[i] < nums[i - 1]:
                    ok = False
                    break
                i += 1

            if ok:
                return c

            m = nums[0] + nums[1]
            k = 0
            i = 1
            while i < len(nums) - 1:
                s = nums[i] + nums[i + 1]
                if s < m:
                    m = s
                    k = i
                i += 1

            nums[k] = m
            nums.pop(k + 1)
            c += 1