import sympy as sy

x1, x2 = sy.symbols('x1 x2')
f = sy.symbols('f',cls=sy.Function)
f = x1**2 + x2**2 - x1*x2 - 10*x1 - 4*x2 + 60

#坐标轮换法，f表示函数，x表示初始点，coordinate是函数变量构成的数组，epsilon是允许最大误差
def CoordinateAlternation(f, x, coordinate, epsilon):
    k = 1
    x_temp = x.copy()
    while True:
        for i in range(x.rows):
            t = OneDimensionSearch(f, x_temp, coordinate, i)
            x_temp[i] = x_temp[i] + t[0]
        count = 0
        for i in range(x.rows):
            count = (x_temp[i] - x[i])**2 + count
        count = count**0.5
        if count <= epsilon:
            return x_temp
        x = x_temp.copy()
        k = k + 1
        print(functionsubs(f,x_temp,coordinate))

#计算函数值
def functionsubs(f,x,coordinate):
    for i in range(x.rows):
        f = f.subs({coordinate[i]:x[i]})
    f_val = f.evalf()
    return f

#函数用于一维搜索，f表示函数，x_temp表示当前点，是数组，coordinate是函数变量构成的数组，index是当前搜索方向
def OneDimensionSearch(f, x_temp, coordinate, index):
    length = x_temp.rows
    t = sy.symbols('t')
    f_val = f
    for i in range(length):
        if i == index:
            x_ord = x_temp[i] + t
            f_val = f_val.subs({coordinate[i]:x_ord})
        else:
            f_val = f_val.subs({coordinate[i]:x_temp[i]})
    f_val = f_val.diff(t,1)
    return sy.solve(f_val,t)

x_temp = sy.Matrix([0.,0.])
coordinate = [x1,x2]
xstar = CoordinateAlternation(f, x_temp, coordinate, 0.1)
print(xstar)