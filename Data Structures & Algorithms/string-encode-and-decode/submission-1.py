''' 
NOTE: I honestly wasn't sure what this was even asking, so followed along with the solution.
'''

DC: str = '#'  # Delimited character

class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        # Add the number of characters, followed by the delimiter character
        for s in strs:
            res += str(len(s)) + DC + s
        return res

    def decode(self, s: str) -> List[str]:
        res, i = [], 0

        # Read each word
        while i < len(s):
            # Get the number of characters in the current word
            j = i
            # Go through all j "digits" until the delimiter is reached
            while s[j] != "#":
                j += 1
            # Get the total integer length of the word
            s_len = int(s[i:j])
            # Append the contents of this string (j characters) to the final string
            res.append(s[j + 1 : j + 1 + s_len])
            i = j + 1 + s_len  # Update the i pointer to the beginning of the next string

        # Return the final array of words
        return res 