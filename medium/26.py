class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = (2**31) - 1
        INT_MIN = -(2**31)

        ret = int(dividend / divisor)

        if ret > INT_MAX:
            return INT_MAX
        elif ret < INT_MIN:
            return INT_MIN         
        else:
            return ret
