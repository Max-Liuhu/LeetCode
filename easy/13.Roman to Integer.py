# 参考链接：https://blog.csdn.net/coder_orz/article/details/51448537
# 记数的方法：
# 1. 相同的数字连写，所表示的数等于这些数字相加得到的数，如 III=3；
# 2. 小的数字在大的数字的右边，所表示的数等于这些数字相加得到的数，如 VIII=8、XIII=12；
# 3. 小的数字（限于 I、X 和 C）在大的数字的左边，所表示的数等于大数减小数得到的数，如 IV=4、IX=9；
# 4. 在一个数的上面画一条横线，表示这个数增值 1,000 倍。
class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        digits = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        sum = 0
        maxDigit = 1
        for i in range(len(s)-1, -1, -1):
            if digits[s[i]] >= maxDigit:
                maxDigit = digits[s[i]]
                sum += digits[s[i]]
            else:
                sum -= digits[s[i]]

        return sum