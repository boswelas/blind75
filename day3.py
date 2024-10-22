from cmath import inf
from typing import List, Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

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
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
        You may assume that each input would have exactly one solution, and you may not use the same element twice.
        You can return the answer in any order."""
        values = {}
        
        for index, num in enumerate(nums):
            if target - num in values:
                return (index, values[target - num])
            else:
                values[num] = index
                  
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next
            
            if fast == slow:
                return True

        return False
    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
            
        curr.next = list1 or list2
        
        return dummy.next
    
solution = Solution()
list1 = [1,2,4]
l1 = ListNode(list1[0])
for val in list1[1:]:
    l1.next = ListNode(val)
    l1 = l1.next 
list2 = [1,3,4]
l2 = ListNode(list2[0])
for val in list2[1:]:
    l2.next = ListNode(val)
    l2 = l2.next 
print(solution.mergeTwoLists(l1, l2))

