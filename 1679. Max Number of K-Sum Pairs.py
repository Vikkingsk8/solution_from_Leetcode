# You are given an integer array nums and an integer k.
#
# In one operation, you can pick two numbers from the
# array whose sum equals k and remove them from the array.
#
# Return the maximum number of operations you can perform on the array.


# solution
# также способ двух точек делаем две точки слева и справа
# делаем цикл до тех пор, пока точки не сомкнутся
# и смотрим если сумма равна k , то увеличиваем счетчик
# если сумма меньше k, то увеличиваем точку слева

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        left = 0
        right = len(nums) - 1
        count = 0
        while left < right:
            if nums[left] + nums[right] == k:
                count += 1
                left += 1
                right -= 1
            elif nums[left] + nums[right] < k:
                left += 1
            else:
                right -= 1
        return count
