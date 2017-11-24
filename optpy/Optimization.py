import sympy as sy

class Optimization(object):
    def __init__(self,useGui,str_fun=None,epsilon=None,result_out=None):
        self.result_out = result_out
        if useGui == False:
            self.f_str = input('请输入你的函数表达式：')
            self.f = sy.simplify(self.f_str)
            self.x = list(self.f.free_symbols)
            print('函数f中发现以下变量', self.x, '请为其赋初始值,以，分隔：')
            self.x_val = input()
            self.x_val = self.x_val.split(',')
            self.x_val = [float(x) for x in self.x_val]
            self.x_length = self.x_val.__len__()
            self.epsilon = float(input('请输入最大误差epsilon：'))
            self.x_star = None
        else:
            self.f_str = str_fun
            self.f = sy.simplify(str_fun)
            self.x = list(self.f.free_symbols)
            self.x_val = [0] * self.x.__len__()
            self.x_length = self.x_val.__len__()
            self.epsilon = float(epsilon)
            self.x_star = None
        f_split = self.f_str.split('**')
        self.maxpow = 0.0 #计算函数最高次数
        for i in range(1,len(f_split)):
            if self.maxpow < float(f_split[i][0]):
                self.maxpow = float(f_split[i][0])

    def calcufun(self):
        f = self.f
        for i in range(self.x_length):
            f = f.subs({self.x[i]:self.x_star[i]})
        return f

    def Newton(self,x, x_val, epsilon, f, d):
        lambda_ = sy.symbols('lambda_')
        x_temp = sy.Matrix(x_val).reshape(len(x), 1) + lambda_ * d
        f_temp = f
        for i in range(len(x)):
            f_temp = f_temp.subs({x[i]: x_temp[i]})
        f_diff = f_temp.diff(lambda_, 1)
        f_diff2 = f_diff.diff(lambda_, 1)
        lambda_val = 0.0
        f_diff_val = f_diff.subs({lambda_: lambda_val})
        while abs(f_diff_val) >= epsilon:
            lambda_val = lambda_val - (f_diff.subs({lambda_: lambda_val}) / (f_diff2.subs({lambda_: lambda_val})+1e-6))
            f_diff_val = f_diff.subs({lambda_: lambda_val})
        lambda_val = lambda_val - (f_diff.subs({lambda_: lambda_val}) / (f_diff2.subs({lambda_: lambda_val}) + 1e-6))
        return lambda_val