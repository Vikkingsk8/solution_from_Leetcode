# Given an array of integers arr,
# return true if the number of
# occurrences of each value in the array is unique or false otherwise.


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = {}
        for elem in arr:
            if elem in counter:
                counter[elem] += 1
            else:
                counter[elem] = 1

        return len(list(counter.values())) == len(set(list(counter.values()))
