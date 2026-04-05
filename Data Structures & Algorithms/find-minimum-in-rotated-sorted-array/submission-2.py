class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Declare l, m, r pointers
        l = 0
        r = len(nums) - 1

        # Iteratively perform a modified BST
        cur_min: int = nums[0]
        while l <= r:
            if nums[l] < nums[r]:
                cur_min = min(cur_min, nums[l])
                break
            
            m = (l + r) // 2
            cur_min = min(cur_min, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        
        # Return the final result
        return cur_min
