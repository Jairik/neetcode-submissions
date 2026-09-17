class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Solution followed along with video
        result = [1] * (len(nums))  # resultult output array, initialized to one

        prefix = 1  # Storesult the current prefix

        # Loop through the nums array (ascending), storing product prefixes in the resultult
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]

        # Loop through the array (descending), calculating postfixes and storing products in resultult
        postfix = 1  # Storesult the current postfix, used to calculate final answer
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]  # Update postfix with current number in the array 

        return result