# Given a binary array nums and an integer k,
# return the maximum number of consecutive 1's in the array if you can flip at most k 0's.



class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start = 0
        for index in range(len(nums)):
            if nums[index] == 0:
                k -= 1
            if k < 0:
                if nums[start] == 0:
                    k += 1
                start += 1

        return index - start + 1