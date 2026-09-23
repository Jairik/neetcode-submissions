'''
Valid Sudoku Notes
- We may assume that all values are either 1-9 or ., so no additional checking needs to be done here
- Must perform checks for rows, columns, and 3x3 grids
- We may exit at any time if any condition is found to be fasle

Naive Approach:
- Nested for-loop to check rows, then columns, then grids.
- O(n^3-ish time complexity)

How can we check all conditions at once?

Optimal Solution:
- Use three hashmaps, one for row, column, and 3x3 grid
'''
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Initialize known number of rows, columns, and 3x3 grids
        num_rows, num_cols, num_grids = 9, 9, 3

        # Create hashsets for rows, columns, and grids 
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        grids = collections.defaultdict(set)

        # Iterate through the entire soduko
        for r in range(num_rows):
            for c in range(num_cols):
                if board[r][c] == ".":
                    continue
                # Check if the current number has already been seen
                elif (board[r][c] in rows[r] or  # Check if it is in the current row
                    board[r][c] in cols[c] or  # Check if it is in the current col
                    board[r][c] in grids[ (r // num_grids, c // num_grids) ]  # Check if it is in the current grid
                ):
                    return False
                # If it is not a duplicate, we can add it to the current row, column, and grid
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                grids[(r // num_grids, c // num_grids)].add(board[r][c])

        # If the entire iteration has completed, we may return true
        return True

