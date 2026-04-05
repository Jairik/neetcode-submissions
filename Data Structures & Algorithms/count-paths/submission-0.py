''' NOTE: Followed along with solution video '''

"""
Approach:
    - Recurve DFS-like path search, taking the sum of possible paths at each R(ight), D(own) combination.
    - This is a heavy conceptual problem, most beneficial to annotate on this first then find a pattern.
    - We can find the total number of unique paths by summing up the unique paths the adjacent cells
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n  # Bottom row (all contain 1 possible path, going right)

        # Calculating the possible paths for each cell in each row
        for i in range(m - 1):
            newRow = [1] * n
            # Go right to left for each 'column'/cell in the row (last column will always be 1, as there is only 1 unique path from these positions)
            for j in range(n - 2, -1, -1):
                newRow[j] = newRow[j + 1] + row[j]
            row = newRow
        
        # Get the total possible combinations at the starting point (top left, last column in last row calculated)
        return row[0]


