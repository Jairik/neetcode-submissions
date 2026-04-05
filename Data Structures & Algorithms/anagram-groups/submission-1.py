from collections import defaultdict
# Time Complexity: O(n*m) | Space Complexity: O(n * m)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_dict = defaultdict(list)
        # Loop through each string
        for s in strs:
            count = [0] * 26  # Make a count array for each letter
            # Assign each letter to the count array
            for c in s:
                count[ord(c) - ord('a')] += 1
            # Make the count array a tuple so we can make it a Hash key
            key = tuple(count)
            # Using the counts as a key, append it to the array
            anagrams_dict[key].append(s)

        return list(anagrams_dict.values())