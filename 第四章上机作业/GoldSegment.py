from sympy import *

x = symbols('x')
f = symbols('f',cls=Function)
f = 3*x**4-4*x**3-12*x**2

#执行黄金分割法f为函数表达式，a，b为初始区间，l为精度要求
def GoldSegment(f, a, b, L):
    lambda_ = a + 0.382 * (b - a)
    miu_ = a + 0.618 * (b - a)
    k = 1
    f_value = 0
    while b - a >= L:
        if f.evalf(subs={x:lambda_}) > f.evalf(subs={x:miu_}):
            a = lambda_
            b = b
            lambda_ = miu_
            miu_ = a + 0.618 * (b - a)
            f_value = f.evalf(subs={x:miu_})
        else:
            a = a
            b = miu_
            miu_ = lambda_
            lambda_ = a + 0.382 * (b - a)
            f_value = f.evalf(subs={x:lambda_})
        k = k + 1
    return [a,b] , f_value

s, f_v = GoldSegment(f,0.0,3.0,0.001)
print('搜索后的最佳区间为：',s,' 此时的函数值为：',f_v)