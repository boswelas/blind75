from typing import List


class Solution:
    
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
                
        return -1
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
        such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
        Notice that the solution set must not contain duplicate triplets."""
        
        nums.sort()
        result = set()
        
        for i in range(0, len(nums) - 2):
            if i - 1 > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] > 0:
                break 
            j = i + 1
            k = len(nums) - 1
            while j < k:
                temp = nums[i] + nums[j] + nums[k]
                if temp == 0:
                    result.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif temp < 0:
                    j += 1
                else:
                    k -= 1
        return [list(val) for val in result]
    
    
solution = Solution()
nums = [-2,0,1,1,2]
print(solution.threeSum(nums))

