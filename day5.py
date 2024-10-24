class Solution:
    
    def longestPalindrome(self, s: str) -> str:
        result = ""
        resLen= 0
        
        for i in range(len(s)):
            l, r = i, i 
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    result = s[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1
                
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    result = s[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1
        return result

    def countSubstrings(self, s: str) -> int:
        """Given a string s, return the number of palindromic substrings in it.
        A string is a palindrome when it reads the same backward as forward.
        A substring is a contiguous sequence of characters within the string."""
        result = 0
        
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                result += 1
                l -= 1
                r += 1
            
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                result += 1
                l -= 1
                r += 1
                
        return result
        


solution = Solution()
s = "aaa"
print(solution.countSubstrings(s))
