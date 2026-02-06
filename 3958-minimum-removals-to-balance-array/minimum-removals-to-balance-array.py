class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        n = len(nums)

        l = 0
        m_l = 0

        for r in range(n):
            while nums[r] > nums[l]*k:
                l += 1
            m_l = max(m_l , r-l+1)

        return n - m_l