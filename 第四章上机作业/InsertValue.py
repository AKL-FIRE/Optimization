from sympy import *

x = symbols('x')
f = symbols('f',cls=Function)
f = 3*x**4-4*x**3-12*x**2

#用抛物线插值法求解f表示函数，t0，t1，t2是初始点，epsilon表示最大误差
def InsertValue(f,t0,t1,t2,epsilon):
    f_val_t0 = f.evalf(subs={x:t0})
    f_val_t1 = f.evalf(subs={x:t1})
    f_val_t2 = f.evalf(subs={x:t2})
    if f_val_t1 < f_val_t0 or f_val_t2 < f_val_t0:
        print('t0不合法')
        return
    while True:
        t_ = 0.5 * ((t0**2 - t2**2) * f_val_t1 + (t2**2 - t1**2) * f_val_t0 + (t1**2 - t0**2) * f_val_t2) / ((t0 - t2) * f_val_t1 + (t2 - t1) * f_val_t0 + (t1 - t0) * f_val_t2)
        if abs(t_ - t0) < epsilon:
            t_star = t_
            f_star = f.evalf(subs={x:t_})
            return t_star, f_star
        else:
            if t_ > t0:
                if f.evalf(subs={x:t_}) <= f_val_t0:
                    t1 = t0
                    t0 = t_
                    f_val_t1 = f_val_t0
                    f_val_t0 = f.evalf(subs={x:t_})
                else:
                    t2 = t_
                    f_val_t2 = f.evalf(subs={x:t_})
            else:
                if f.evalf(subs={x:t_}) <= f_val_t0:
                    t2 = t0
                    t0 = t_
                    f_val_t2 = f_val_t0
                    f_val_t0 = f.evalf(subs={x: t_})
                else:
                    t1 = t_
                    f_val_t1 = f.evalf(subs={x:t_})

t_star, f_star = InsertValue(f,1.0,0.0,3.0,0.01)
print('搜索后的最佳点为：', t_star, ' 此时的函数值为：', f_star)