class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [0] * n
        l = 0 
        r  = idx = n - 1 
        while (l <= r):
            if abs(nums[l]) > abs(nums[r]):
                answer[idx] = nums[l] ** 2
                l += 1
            else:
                answer[idx] = nums[r] ** 2
                r -= 1
            idx -= 1
        return answer
