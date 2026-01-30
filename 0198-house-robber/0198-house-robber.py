class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return max(nums)

        dp = [0] * (n+1) 
        dp[0] = nums[0]
        dp[1] = nums[1]

        for i in range(n):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        return dp[n-1]

