class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_len = len(s)
        start_index: int = 0
        end_index: int = s_len - 1
        
        # Begin the comparison loop
        while(start_index < end_index):

            first_char = s[start_index].lower()
            second_char = s[end_index].lower()

            # Handle edge cases of spaces
            if not first_char.isalnum():
                start_index += 1
                continue
            elif not second_char.isalnum():
                end_index -= 1
                continue

            # A palindrome rule has been violated, return false
            if first_char != second_char:
                return False

            # Increment start pointer and decrement end pointer
            start_index += 1    
            end_index -= 1

        # All conditions have been met
        return True