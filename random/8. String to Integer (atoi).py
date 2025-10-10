class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0

        sign, i, n, res = 1, 0, len(s), 0
        INT_MAX, INT_MIN = 2**31 - 1, -(2**31)
        if s[0] in ("+", "-"):
            sign = 1 if s[0] == "+" else -1
            i += 1
        while i < n and s[i].isdigit():
            res = res * 10 + int(s[i])
            if sign * res > INT_MAX:
                return INT_MAX
            if sign * res < INT_MIN:
                return INT_MIN
            i += 1

        return sign * res
