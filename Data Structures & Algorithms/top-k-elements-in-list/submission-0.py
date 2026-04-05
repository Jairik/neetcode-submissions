''' 
OLD Approach (n time complexity): 
    - Loop through the array once, storing counts in a hashmap
    - Pop the k elements with highest occurences
    - Add to list and return

OLD Alternative Less-Optimal Approach:
    - Sort the list, then return first k unique elements (nlogn time complexity)

OLD CODE:
    occurences: dict = {}  # Track the number of occurences of each number
        res: list = []

        # Get the total number of occurences for each number in the 
        for n in nums:  
            if n in occurences:
                occurences[n] = occurences[n] + 1
            else:
                occurences[n] = 0

        # Get the k highest occurences in a list format
        for i in range(k):
            
NEW OPTIMAL APPROACH:
    - Using a modified Bucket Sort method
'''

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        NUMS_SIZE = len(nums)
        count: dict = {}
        freq_arr: list = [[] for i in range(NUMS_SIZE + 1)]
        max_occurences: int = 1  # Tracker for the top index (occurences)

        # Add the number of occurences into the count hashmap
        for n in nums:
            count[n] = 1 + count.get(n, 0)
            max_occurences = count[n] if count[n] > max_occurences else max_occurences  # Keep track of the total index to prevent extra loops

        # Get all key value pairs, inserting it into the frequency array
        for n, c in count.items():
            freq_arr[c].append(n)

        # Get the top k frequencies to return
        res = []
        res_len = 0
        for i in range(max_occurences, 0, -1):
            for n in freq_arr[i]:
                res.append(n)
                res_len += 1
                if res_len == k:
                    return res

