# Given an input string s, reverse the order of the words.
# A word is defined as a sequence of non-space characters.
# The words in s will be separated by at least one space.
# Return a string of the words in reverse order concatenated by a single space.
# Note that s may contain leading or trailing spaces or multiple spaces between two words.
# The returned string should only have a single space separating the words.
# Do not include any extra spaces.


# требуется вернуть строку со словамма в обратном порядке без дополнительных пробелов
# использовать методов split, reverse, join
# берем метод join соединяем список разбитый сплитом и через отрицательный шаг перевернуть

# code

class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])