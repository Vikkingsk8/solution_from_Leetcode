#You have a long flowerbed in which some of the plots are planted, and some are not.
# However, flowers cannot be planted in adjacent plots.
# Given an integer array flowerbed containing 0's and 1's,
# where 0 means empty and 1 means not empty, and an integer n,
# return true if n new flowers can be planted in the flowerbed without
# violating the no-adjacent-flowers rule and false otherwise.


#требуется узнать возможно ли посадить  n цветов в массивов цветов, вернуть True или False
# если цветов нет, то вернуть True
# для этого я сделал 2 переменные длины массива и количествопросадимых цветов
# далее в цикле пробегаюсь по массиву и смотрю пустые ячейки
#code

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        length = len(flowerbed)
        quantity = n
        if quantity == 0:
            return True

        for i in range(length):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == length - 1 or flowerbed[i + 1] == 0):
                flowerbed[i] = 1
                quantity -= 1
                if quantity == 0:
                    return True
        return False
