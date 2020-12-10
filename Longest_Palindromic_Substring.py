
#Given a string s, return the longest palindromic substring in s.

#Example

#Input: s = "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.

# Input: s = "cbbd"
# Output: "bb"

class Solution:

    def reverse(s):
        stri = ""
        for i in s:
            stri = i + stri
        print(stri)
        return stri
    #reverse('badmon')

    def isPalindrome(s):
        if stri == s:
            return True
        else: 
            return False
    isPalindrome('bab')

    # def longestPalindrome(s):
    #     lpalindrome = s[0]
    #     max_len = 0
    #     for i in range(len(s)):
    #         for j in range(i+1, len(s)):
    #             substring = s[i:j]
    #         if isPalindrome(s) and max_len < len(substring):
    #             max_len = len(substring)
    #             lpalindrome = substring
    #     return lpalindrome
    # longestPalindrome('bab')

                