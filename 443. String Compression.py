# Given an array of characters chars, compress it using the following algorithm:
#
# Begin with an empty string s. For each group of consecutive repeating characters in chars:
#
# If the group's length is 1, append the character to s.
# Otherwise, append the character followed by the group's length.
# The compressed string s should not be returned separately, but instead,
# be stored in the input character array chars. Note that group lengths that are 10
# or longer will be split into multiple characters in chars.
#
# After you are done modifying the input array, return the new length of the array.
#
# You must write an algorithm that uses only constant extra space.


# code

# class Solution:
#     def compress(self, chars: List[str]) -> int:
#         res = []
#         for i in chars:
#             count = chars.count(i)
#             if i not in res:
#                 res.append(i)
#                 res.append(str(count))
#
#         return len(res)
# не понимаю почему этот код не прошел тест(


# code 2
# Пока не разобрался с кодом

class Solution:

    def compress(self, chars: List[str]) -> int:

        res = []
        count = 1
        for i in range(len(chars)):
            if i == len(chars) - 1 or chars[i] != chars[i + 1]:
                res.append(chars[i])
            if count > 1:
                res.extend(list(str(count)))
                count = 1
            else:
                count += 1
        chars[:] = res
        return len(res)
