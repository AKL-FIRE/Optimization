import optpy.Optimization as op
import sympy as sy

class DFP(op.Optimization):
    '''此函数用来执行DFP算法，请保证你的函数阶数小于3'''
    def __init__(self,useGUI,str_fun=None,epsilon=None):
        super(DFP,self).__init__(useGUI, str_fun, epsilon)
        if useGUI == False:
            self.x_val1 = []
            self.f_gradient = None
            self.f_gradient1 = None
            print('该算法初始化完成。')
        else:
            self.x_val1 = []
            self.f_gradient = None
            self.f_gradient1 = None
            print('该算法初始化完成。')

    def Calculate(self):
        H = sy.eye(self.x_length)
        f_gradient = sy.Matrix([self.f])
        f_gradient = f_gradient.jacobian(self.x)
        f_gradient_value = f_gradient.copy()
        for i in range(self.x_length):
            f_gradient_value = f_gradient_value.subs({self.x[i]:self.x_val[i]})
        k = 1
        self.f_gradient = f_gradient_value
        while True:
            d = -1.0 * H * f_gradient_value.transpose()
            lambda_ = self.OneDimensionSearch(d)
            self.x_val1 = list(sy.Matrix(self.x_val).reshape(self.x_length,1) + lambda_[0] * d)
            f_gradient_value = f_gradient
            for i in range(self.x_length):
                f_gradient_value = f_gradient_value.subs({self.x[i]: self.x_val1[i]})
            self.f_gradient1 = f_gradient_value
            if f_gradient_value.norm().evalf() <= self.epsilon:
                self.x_star = self.x_val1
                print('经过', k, '次迭代后得到的', '最优解的点为： ', self.x, ' = ', self.x_star, ' 此点处函数值为：', self.calcufun())
                output_str = '经过' + str(k) + '次迭代后得到的最优解的点为： ' + str(self.x) + '=' + str(
                    self.x_star) + ' 此点处函数值为：' + str(self.calcufun())
                return self.x_star, self.calcufun(), output_str
            else:
                p = sy.Matrix(self.x_val1).reshape(self.x_length,1) - sy.Matrix(self.x_val).reshape(self.x_length,1)
                q = (self.f_gradient1 - self.f_gradient).transpose()
                H = H + ((p * p.T) / (p.T * q)[0]) - ((H * q * q.T * H) / (q.T * H * q)[0])
                k = k + 1
                self.x_val = self.x_val1
                self.f_gradient = self.f_gradient1

    def OneDimensionSearch(self,d):
        lambda_ = sy.symbols('lambda_')
        x_temp = sy.Matrix(self.x_val).reshape(self.x_length,1) + lambda_ * d
        f_temp = self.f
        for i in range(self.x_length):
            f_temp = f_temp.subs({self.x[i]:x_temp[i]})
        f_diff = f_temp.diff(lambda_,1)
        return sy.solve(f_diff,lambda_)