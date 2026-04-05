# NOTE: SEMI-REVIEWED ANSWER
# Approach: Two pointer 
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Tracking Variables
        numbers_size = len(numbers)  # Get length of array once
        left_ptr: int = 0  # Index tracker for left
        right_ptr: int = numbers_size - 1  # Index tracker fo right
        final_indexes: list() = []  # Empty list to hold final indexes

        # Iterate while the left is less than the right (cannot use same element twice)
        while left_ptr < right_ptr:
            cur_sum = numbers[left_ptr] + numbers[right_ptr]
            # Base case: If target is reached
            if cur_sum == target:
                final_elements = [(left_ptr + 1), (right_ptr + 1)]
                break
            # If the sum is less than, move the left ptr (undershot)
            if cur_sum < target:
                left_ptr += 1
            # If the sum is more than, move the right ptr (overshot)
            if cur_sum > target:
                right_ptr -= 1
            

        # return the result
        return final_elements