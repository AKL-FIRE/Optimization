import sympy as sy

class Optimization(object):
    def __init__(self,useGui,str_fun=None,epsilon=None):
        if useGui == False:
            f_str = input('请输入你的函数表达式：')
            self.f = sy.simplify(f_str)
            self.x = list(self.f.free_symbols)
            print('函数f中发现以下变量', self.x, '请为其赋初始值,以，分隔：')
            self.x_val = input()
            self.x_val = self.x_val.split(',')
            self.x_val = [float(x) for x in self.x_val]
            self.x_length = self.x_val.__len__()
            self.epsilon = float(input('请输入最大误差epsilon：'))
            self.x_star = None
        else:
            self.f = sy.simplify(str_fun)
            self.x = list(self.f.free_symbols)
            self.x_val = [0] * self.x.__len__()
            self.x_length = self.x_val.__len__()
            self.epsilon = float(epsilon)
            self.x_star = None

    def calcufun(self):
        f = self.f
        for i in range(self.x_length):
            f = f.subs({self.x[i]:self.x_star[i]})
        return f