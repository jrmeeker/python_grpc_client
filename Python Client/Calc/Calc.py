from waferslim.converters import convert_arg, convert_result, StrConverter

_STR_CONVERTER = StrConverter()

class Calc:
    def __init__(self):
        self._A = 0
        self._B = 0

    @convert_arg(to_type=int)
    def setA(self, A):
        self._A = A

    @convert_arg(to_type=int)
    def setB(self, B):
        self._B = B

    @convert_result(using=_STR_CONVERTER)
    def multiply(self):
        return self._A * self._B

    def execute(self):
        print('Execute function')

    def reset(self):
        print('Reset function')


class Compare:
    def __init__(self):
        self._x = ''
        self._y = ''

    @convert_arg(to_type=str)
    def set_x(self, x):
        self._x = x

    @convert_arg(to_type=str)
    def set_y(self, y):
        self._y = y

    @convert_result(using=_STR_CONVERTER)
    def equal(self):
        return self._x == self._y

    @convert_result(using=_STR_CONVERTER)
    def greater(self):
        return self._x > self._y

    @convert_result(using=_STR_CONVERTER)
    def less(self):
        return self._x < self._y
