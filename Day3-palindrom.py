class Solution:
    def isPalindrome(self, s: str) -> bool:
        leftP = 0
        rightP = -1
        while leftP - rightP < len(s):
            while not s[leftP].isalnum() and leftP - rightP < len(s):
                leftP += 1
            while not s[rightP].isalnum() and  leftP - rightP < len(s) :
                rightP -= 1
            if(s[leftP].lower() != s[rightP].lower()):
                return False
            leftP += 1
            rightP -= 1
        return True

questionlink = 'https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/549/week-1-august-1st-august-7th/3411'