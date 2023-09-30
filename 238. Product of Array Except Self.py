# Given an integer array nums, return an array answer such that answer[i] is equal to the product
# of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

# Здесь сложность заключается в том что нужно получить произведение всех элементов массива,
# у меня возникла сложность с индексами , не очень понимал как перемещаться по списку,
# поэтому вспомогательный список создал
# code

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lenght = len(nums)
        result = [1] * lenght
        left = 1
        right = 1
        for i in range(lenght):
            result[i] *= left
            left *= nums[i]
            result[lenght - i - 1] *= right
            right *= nums[lenght - i - 1]
        return result
