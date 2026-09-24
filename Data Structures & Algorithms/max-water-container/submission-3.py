'''
This seems like a pretty simple two-pointer problem.
Constraints:
- Always at least 2 elements
- Height CAN be 0
'''
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Set the initial maximum water result
        max_water = 0
        # Set the left and right pointers for iterating through the array
        left_ptr = 0
        right_ptr = len(heights) -1

        # Begin looping through the array
        while(left_ptr < right_ptr):
            # Compute the current water volume
            cur_water = min(heights[left_ptr], heights[right_ptr]) * (right_ptr - left_ptr)
            if max_water < cur_water:
                max_water = cur_water
            # Move the pointer of the smaller height
            if heights[right_ptr] >= heights[left_ptr]:
                left_ptr += 1
            else:
                right_ptr -= 1
        
        return max_water