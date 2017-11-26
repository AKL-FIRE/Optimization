import optpy.Optimization as op
import sympy as sy

class BFGS(op.Optimization):
    def __init__(self,useGUI,str_fun=None,epsilon=None):
        super(BFGS,self).__init__(useGUI, str_fun, epsilon)
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
        self.B = sy.eye(self.x_length)
        f_gradient = sy.Matrix([self.f])
        f_gradient = f_gradient.jacobian(self.x)
        f_gradient_value = f_gradient.copy()
        for i in range(self.x_length):
            f_gradient_value = f_gradient_value.subs({self.x[i]:self.x_val[i]})
        k = 1
        self.f_gradient = f_gradient_value
        while True:
            d = -1.0 * self.B.inv() * f_gradient_value.transpose()
            if self.maxpow == 2: #该为2
                lambda_ = self.OneDimensionSearch(d)
                self.s = lambda_[0] * d
                self.x_val1 = list(sy.Matrix(self.x_val).reshape(self.x_length, 1) + lambda_[0] * d)
            else:
                lambda_ = self.Newton(self.x,self.x_val,self.epsilon,self.f,d)
                self.s = lambda_ * d
                self.x_val1 = list(sy.Matrix(self.x_val).reshape(self.x_length, 1) + lambda_ * d)
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
                self.y = (self.f_gradient1 - self.f_gradient).transpose()
                self.B = self.B + ((self.y * self.y.T) / ((self.y.T * self.s)[0]+1e-6)) - ((self.B * self.s * self.s.T * self.B) / ((self.s.T * self.B * self.s)[0]+1e-6))
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