from collections import defaultdict
from typing import List


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_dict = defaultdict(list)
        
        for val in strs:
            sorted_dict["".join(sorted(val))].append(val)
            
        return [val for val in sorted_dict.values()]
        
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        
        while l < r:
            while not s[l].isalnum() and l < r:
                l += 1
            while not s[r].isalnum() and l < r:
                r -= 1
            if s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False
        return True
            
    def isValid(self, s: str) -> bool:
        pairs = {")":"(", "}":"{", "]":"["}
        stack = []
        
        for p in s:
            if p in pairs:
                if stack and stack[-1] == pairs[p]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(p)
        return not stack
        



solution = Solution()
s = "babad"
print(solution.longestPalindrome(s))

