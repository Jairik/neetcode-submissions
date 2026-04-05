class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res: list() = []  # Track the results
        nums.sort()  # Sort the array in memory
        nums_size: int = len(nums)  # Constant for size of nums array

        for i, a in enumerate(nums):
            # Skip over repeat numbers
            if i > 0 and a == nums[i - 1]:
                continue

            # Sorted two-sum implementation (two-sum II with continuous search)
            left_ptr: int = i + 1
            right_ptr: int = nums_size - 1

            while left_ptr < right_ptr:
                cur_sum: int = a + nums[left_ptr] + nums[right_ptr]
                if cur_sum == 0:
                    res.append([a, nums[left_ptr], nums[right_ptr]])
                    # Now, must update indexes to continue searching
                    left_ptr += 1
                    while nums[left_ptr] == nums[left_ptr - 1] and left_ptr < right_ptr:
                        left_ptr += 1
                elif cur_sum < 0:
                    left_ptr += 1
                elif cur_sum > 0:
                    right_ptr -= 1
                else:
                    print("Error - idk how this happened")

        return res  # Return the result (list of lists)