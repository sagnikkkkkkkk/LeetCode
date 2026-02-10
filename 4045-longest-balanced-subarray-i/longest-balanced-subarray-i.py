class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        
        n = len(nums)
        ans = 0

        for i in range(n):
            e = set()
            o = set()

            for j in range(i , n):
                if nums[j] % 2 == 0:
                    e.add(nums[j])
                else:
                    o.add(nums[j])

                if len(e) == len(o):
                    ans = max(ans , j-i+1)

        return ans