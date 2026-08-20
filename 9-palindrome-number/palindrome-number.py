class Solution:
    def isPalindrome(self, x: int) -> bool:
        #pratik
        #method 1  low memory performance 
        # s=str(x)
        # return s==s[::-1]
        

        #method 2 high memory performance
        # if x < 0:
        #  return false
        original = x
        reverse = 0
        while x > 0:
            last_digit = x % 10
            reverse = (reverse * 10) + last_digit
            x //=10

        return original == reverse


      