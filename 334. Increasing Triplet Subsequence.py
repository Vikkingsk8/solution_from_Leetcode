# Given an integer array nums, return true
# if there exists a triple of indices (i, j, k)
# such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.


# Требуется опредилить идут ли по порядку три элемента массива
# Здесь логика решения такая: берем два числа положительных в бесконечность
# проходим по массиву и проверяем меньше или равно текущее число бесконечности(first)
# Если да ,то присваеваем его переменной (first)
# потом идет вторая итерация по списку проверяем также число присваеваем переменной (second)
# И самый главный момент идет третья итерация по списку и проверяем третье число,
# исходя из результата возвращаем true or false

# code
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = float('inf')
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        return False
