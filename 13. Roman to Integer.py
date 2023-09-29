13. Roman to Integer


class Solution:
    def romanToInt(self, s: str) -> int:
        roman_nums = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000} # делаем словарь с единицами ,десятками , сотнями и тысячами
        result = 0                                                              # счетчик
        for key, value in enumerate(s):                                         # здесь функция enumerate перебирает индекс и элемент строки
            if key+1 == len(s) or roman_nums[value] >= roman_nums[s[key+1]]:    # если индекс+1 == длинне s или наш словарь с ключом['I'] больше или равно словарю с ключом['III'[0+1]]
                result += roman_nums[value]                                     # то плюсуем к результату значения из словаря по ключу значения от нашей строки
            else:
                result -= roman_nums[value]                                     # либо отнимаем от результата значение
        return result
