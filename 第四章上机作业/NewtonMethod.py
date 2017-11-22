from sympy import *

x = symbols('x')
f = symbols('f',cls=Function)
f = 3*x**4-4*x**3-12*x**2

#用牛顿法计算最优值f为函数，a为初始点坐标,epsilon为最大允许误差
def NewtonMethod(f,a,epsilon):
    f_diff1 = f.diff(x,1)
    f_diff2 = f.diff(x,2)
    k = 1
    f_diff1_value = f_diff1.evalf(subs={x:a})
    f_diff2_value = f_diff2.evalf(subs={x:a})
    while f_diff1_value >= epsilon:
        d = - f_diff1_value / f_diff2_value
        a = a + d
        k = k + 1
        f_diff1_value = f_diff1.evalf(subs={x: a})
        f_diff2_value = f_diff2.evalf(subs={x: a})
    return a, f.evalf(subs={x:a})

s, f_v = NewtonMethod(f, 3.0, 0.1)
print('搜索后的最佳点为：',s,' 此时的函数值为：',f_v)