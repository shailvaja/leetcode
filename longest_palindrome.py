class Solution:
    def longestPalindrome(self, s: str) -> str:
        output = ""
        def palin(s):
            if len(s)==1:
                return True
            if s[0] == s[-1]:
               return palin(s[1:-1])
            else:
                return False
        
        for x in range(len(s)):
            for y in range(len(s), x, -1):
                if palin(s[x:y])==True:
                    if len(output) < len(s[x:y]):
                        output = s[x:y]
        return output


s = Solution()
print(s.longestPalindrome("cbbd"))