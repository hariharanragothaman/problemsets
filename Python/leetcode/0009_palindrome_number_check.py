class Solution:
    def isPalindrome(self, x: int) -> bool:
        input_list = [char for char in str(x)]
        reversed_list = input_list[::-1]
        if input_list == reversed_list:
            return True
        return False
