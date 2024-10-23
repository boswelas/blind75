class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        return sorted(s) == sorted(t)


solution = Solution()
s = "anagram" 
t = "nagaram"
print(solution.isAnagram(s, t))

