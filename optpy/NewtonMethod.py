import optpy.Optimization as op
import sympy as sy

class NewtonMethod(op.Optimization):
    def __init__(self,useGUI,str_fun=None,epsilon=None):
        super(NewtonMethod, self).__init__(useGUI, str_fun, epsilon)
        if useGUI == False:
            print('该算法初始化完成。')
        else:
            print('该算法初始化完成。')

    def Calculate(self):
        k = 1
        f_diff1 = sy.Matrix([self.f])
        f_diff1 = f_diff1.jacobian(self.x)
        f_diff2 = f_diff1.jacobian(self.x)
        while True:
            d = -1 * f_diff2**-1 * f_diff1.T
            for i in range(self.x_length):
                d = d.subs({self.x[i]: self.x_val[i]})
            if d.norm() <= self.epsilon:
                self.x_star = self.x_val
                print('经过', k, '次迭代后得到的', '最优解的点为： ', self.x, ' = ', self.x_star, ' 此点处函数值为：', self.calcufun())
                output_str = '经过' + str(k) + '次迭代后得到的最优解的点为： ' + str(self.x) + '=' + str(
                    self.x_star) + ' 此点处函数值为：' + str(self.calcufun())
                return self.x_star, self.calcufun(), output_str
            self.x_val = list(sy.Matrix(self.x_val).reshape(self.x_length, 1) + d)
            k = k + 1