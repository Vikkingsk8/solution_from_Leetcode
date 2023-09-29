# There are n kids with candies.
# You are given an integer array candies, where each candies[i] represents the number
# of candies the ith kid has, and an integer extraCandies,
# denoting the number of extra candies that you have.

# Return a boolean array result of length n, where result[i] is true if,
# after giving the ith kid all the extraCandies,
# they will have the greatest number of candies among all the kids, or false otherwise.

# В этой задаче нужно найти максимальное число конфет из списка(детей с конфетами) и сравнить
# сумму количества конфет с экстраКонфетами.
# То есть есть список [2,3,5,1,3] и экстраКонфета = 3,
# проходимся по списку прибавляя екстраКонфету каждому ребенку,
# и сравниваем с максимальным числом конфет из начального списка, если результат больше или равно
# то возвращаем True,
# иначе False.


# code

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        result = []
        for i in candies:
            if i + extraCandies >= max_candies:
                result.append(True)
            else:
                result.append(False)
        return result
