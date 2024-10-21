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

    def maxProduct(self, nums: List[int]) -> int:
        """Given an integer array nums, find a subarray that has the largest product, and return the product.
        The test cases are generated so that the answer will fit in a 32-bit integer."""
        result = max(nums)
        curMin, curMax = 1, 1
        
        for num in nums:
            temp = curMax * num
            curMax = max(temp, num * curMin, num)
            curMin = min(temp, num * curMin, num)
            result = max(result, curMax)
        return result
            
    def findMin(self, nums: List[int]) -> int:
        """Given the sorted rotated array nums of unique elements, return the minimum element of this array."""
        result = nums[0]
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = l + ((r - l) // 2)
            result = min(result, nums[mid])
            if nums[mid] > nums[l]:
                if nums[mid] > nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if nums[mid] < nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return result
        


solution = Solution()
nums = [4,5,6,7,0,1,2]
print(solution.findMin(nums))
