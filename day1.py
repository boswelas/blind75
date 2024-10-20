from cmath import inf
from collections import defaultdict
from typing import List, Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def findMin(self, nums: List[int]) -> int:
        """Suppose an array of length n sorted in ascending order is rotated between 1 and n times. 
        For example, the array nums = [0,1,2,4,5,6,7] might become:
        [4,5,6,7,0,1,2] if it was rotated 4 times.
        [0,1,2,4,5,6,7] if it was rotated 7 times.
        Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
        Given the sorted rotated array nums of unique elements, return the minimum element of this array.
        You must write an algorithm that runs in O(log n) time."""
        l, r = 0, len(nums) - 1
        result = nums[0]
        
        while l <= r:
            mid = l + ((r - l) // 2)
            result = min(result, nums[mid])
            if nums[l] < nums[mid]:
                if nums[r] < nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if nums[r] > nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
        return result
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Given the head of a singly linked list, reverse the list, and return the reversed list."""
        prev = None
        curr = head
        
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        """Given a string s, find the length of the longest substring without repeating characters."""
        result = 0
        chars = set()
        l = 0
        
        for r in range(0, len(s)):
            if s[r] not in chars:
                chars.add(s[r])
                result = max(result, r - l + 1)
            else:
                while s[r] in chars:
                    chars.remove(s[l])
                    l += 1
                chars.add(s[r])
        return result

    def characterReplacement(self, s: str, k: int) -> int:
        """You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. 
        You can perform this operation at most k times.
        Return the length of the longest substring containing the same letter you can get after performing the above operations."""
        sMap = defaultdict(int)
        result = 0
        l = 0
        maxVal = 0
        
        for r in range(0, len(s)):
            sMap[s[r]] += 1
            maxVal = max(maxVal, sMap[s[r]])
            if (r - l + 1) - maxVal > k:
                sMap[s[l]] -= 1
                l += 1
            result = max(result, r - l + 1)
        return result        
                    
    def maxProfit(self, prices: List[int]) -> int:
        """You are given an array prices where prices[i] is the price of a given stock on the ith day.
        You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
        Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0."""
        result = 0
        l = 0
        r = 1
        
        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
            else:
                result = max(result, (prices[r] - prices[l]))
            r += 1
        
        return result
   
    def containsDuplicate(self, nums: List[int]) -> bool:
        """Given an integer array nums, return true if any value appears at least twice in the array, 
        and return false if every element is distinct."""
        numSet = set()
        
        for num in nums:
            if num not in numSet:
                numSet.add(num)
            else:
                return True
        return False
        
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
        The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
        You must write an algorithm that runs in O(n) time and without using the division operation."""
        
        prefix = [1]
        suffix = [1]
        
        for num in nums:
            prefix.append(num * prefix[-1])
            
        for i in range(len(nums)-1, -1, -1):
            suffix.append(nums[i] * suffix[-1])
        suffix = suffix[::-1]
        print(prefix)
        print(suffix)
        
        for i in range(1, len(suffix)):
            prefix[i  - 1] = prefix[i - 1] * suffix[i]
        return prefix[:-1]


       


solution = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(solution.maxSubArray(nums))

# head = [1,2,3,4,5]
# list1 = ListNode(head[0])
# current = list1
# for val in head[1:]:
#     current.next = ListNode(val)
#     current = current.next
# curr = list1
# print(solution.reverseList(list1))



