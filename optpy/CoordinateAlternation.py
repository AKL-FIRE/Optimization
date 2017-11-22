import optpy.Optimization as op
import sympy as sy

class CoordinateAlternation(op.Optimization):
    def __init__(self,useGUI,str_fun=None,epsilon=None):
        super(CoordinateAlternation,self).__init__(useGUI, str_fun, epsilon)
        if useGUI == False:
            self.x_val1 = self.x_val
            print('该算法初始化完成。')
        else:
            self.x_val1 = self.x_val
            print('该算法初始化完成。')

    def Calculate(self):
        k = 1
        while True:
            for e in self.x:
                x_temp = self.OneDimensionSearch(e)
                self.x_val1 = list(x_temp)
            if (sy.Matrix(self.x_val1).reshape(self.x_length,1) - sy.Matrix(self.x_val).reshape(self.x_length,1)).norm() <= self.epsilon:
                self.x_star = self.x_val1
                print('经过', k, '次迭代后得到的', '最优解的点为： ', self.x, ' = ', self.x_star, ' 此点处函数值为：', self.calcufun())
                output_str = '经过' + str(k) + '次迭代后得到的最优解的点为： ' + str(self.x) + '=' + str(
                    self.x_star) + ' 此点处函数值为：' + str(self.calcufun())
                return self.x_star, self.calcufun(), output_str
            else:
                k = k + 1
                self.x_val = self.x_val1

    def OneDimensionSearch(self,e):
        t = sy.symbols('t')
        index = self.x.index(e)
        e_vec = sy.zeros(self.x_length,1)
        e_vec[index] = 1
        x_temp = sy.Matrix(self.x_val1).reshape(self.x_length,1) + t * e_vec
        f = self.f
        for i in range(self.x_length):
            f = f.subs({self.x[i]:x_temp[i]})
        f_diff = f.diff(t,1)
        t_star =  sy.solve(f_diff,t)
        return x_temp.subs({t:t_star[0]})