# You are given an integer array height of length n.
# There are n vertical lines drawn such that the two
# endpoints of the ith line are (i, 0) and (i, height[i]).
#
# Find two lines that together with the x-axis form a container,
# such that the container contains the most water.
#
# Return the maximum amount of water a container can store.


# solution
# Решение две точки .Делаем две точки лево и право
# также счетчик максимальной площади
# вычисляем максимальную площадь и проверяем ее с помощью функции max
# Если точка лево меньше точки право, то двигаем левую точку вправо




class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0
        while left < right:
            max_area = max(max_area, (right - left) * min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
