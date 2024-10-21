from typing import List

class Solution:

    def maxSubArray(self, nums: List[int]) -> int:
        """Given an integer array nums, find the subarray with the largest sum, and return its sum."""
        result = nums[0]
        temp = 0
        
        for num in nums:
            if temp < 0:
                temp = 0
            temp += num
            result = max(result, temp)
        return result

solution = Solution()
nums = [-2,-1]
print(solution.maxSubArray(nums))
