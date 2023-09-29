class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 1
        stroka = ''
        if len(set(s)) == len(s):
            return len(s)
            
        for i in s:
            if i not in stroka:
                stroka += i
                max_len = max(max_len, len(stroka))
            else:
                stroka = stroka.split(i)[1]+i
        return max_len
