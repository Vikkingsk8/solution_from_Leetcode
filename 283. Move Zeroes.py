# Given an integer array nums, move all 0's ' \
# to the end of it while maintaining the relative order of the non-zero elements.
#
# Note that you must do this in-place without making a copy of the array.

#code
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        if len(nums) == 0:
            return nums

        zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[zero], nums[i] = nums[i], nums[zero]
                zero += 1

        return nums
