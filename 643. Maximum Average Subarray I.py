def findMaxAverage(nums=[1, 12, -5, -6, 50, 3], k=4):
    sum = 0
    for i in range(k):
        sum += nums[i]
    max_sum = sum
    for i in range(k, len(nums)):
        sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, sum)
    return max_sum / k


print(findMaxAverage())
