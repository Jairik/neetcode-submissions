class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_size = len(s)  # Length of the string
        l: int = 0  # Left pointer
        max_len = 1  # Track the largest substring
        char_set = set()  # Hash set to keep track of characters

        # Handle edge case
        if s_size < 2:
            max_len = s_size

        else:
            # Begin logic (sliding window)
            for r in range(len(s)):
                while s[r] in char_set:
                    char_set.remove(s[l])
                    l += 1
                char_set.add(s[r])
                cur_len = (r - l + 1)
                if cur_len > max_len: max_len = cur_len


        # Return the final result
        return max_len
                
