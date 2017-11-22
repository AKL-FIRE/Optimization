import optpy.Optimization as op
import sympy as sy
import random

class InsertValue(op.Optimization):
    def __init__(self,useGUI,str_fun=None,epsilon=None):
        super(InsertValue, self).__init__(useGUI, str_fun, epsilon)
        if self.x.__len__() != 1:
            raise('非法的参数个数，只允许单变量函数。')
        self.t_star = 0
        self.f_star = 0
        if useGUI == False:
            self.t1 = self.GetX()[0]
            self.t2 = self.GetX()[1]
            self.t0 = (self.t1 + self.t2) / 2
            print('该算法初始化完成。')
        else:
            self.t1 = self.GetX()[0]
            self.t2 = self.GetX()[1]
            self.t0 = (self.t1 + self.t2) / 2
            print('该算法初始化完成。')

    #加步探索法寻找区间
    def GetX(self):
        k = 0
        t = 0
        t0 = random.random() * 10
        f_value0 = self.f.subs({self.x[0]: t0})
        h0 = 1.0
        while True:
            if k>= 10000:
                raise('未找到单谷区间')
            t1 = t0 + h0
            f_value1 = self.f.subs({self.x[0]:t1})
            if f_value1 < f_value0:
                h0 = 2 * h0
                t = t0
                t0 = t1
                f_value0 = f_value1
                k = k + 1
            else:
                if k == 0:
                    h0 = -1 * h0
                    t = t1
                else:
                    return min(t,t1),max(t,t1)

    def Calculate(self):
        f_val_t0 = self.f.evalf(subs={self.x[0]: self.t0})
        f_val_t1 = self.f.evalf(subs={self.x[0]: self.t1})
        f_val_t2 = self.f.evalf(subs={self.x[0]: self.t2})
        t0 = self.t0
        t1 = self.t1
        t2 = self.t2
        if f_val_t1 < f_val_t0 or f_val_t2 < f_val_t0:
            print('t0不合法')
            return
        while True:
            t_ = 0.5 * (
            (t0 ** 2 - t2 ** 2) * f_val_t1 + (t2 ** 2 - t1 ** 2) * f_val_t0 + (t1 ** 2 - t0 ** 2) * f_val_t2) / (
                 (t0 - t2) * f_val_t1 + (t2 - t1) * f_val_t0 + (t1 - t0) * f_val_t2)
            if abs(t_ - t0) < self.epsilon:
                self.t_star = t_
                self.f_star = self.f.evalf(subs={self.x[0]: t_})
                output_str = '搜索后的最佳点为：'+ str(self.t_star)+' 此时的函数值为：'+str(self.f_star)
                return self.t_star, self.f_star, output_str
            else:
                if t_ > t0:
                    if self.f.evalf(subs={self.x[0]: t_}) <= f_val_t0:
                        t1 = t0
                        t0 = t_
                        f_val_t1 = f_val_t0
                        f_val_t0 = self.f.evalf(subs={self.x[0]: t_})
                    else:
                        t2 = t_
                        f_val_t2 = self.f.evalf(subs={self.x[0]: t_})
                else:
                    if self.f.evalf(subs={self.x[0]: t_}) <= f_val_t0:
                        t2 = t0
                        t0 = t_
                        f_val_t2 = f_val_t0
                        f_val_t0 = self.f.evalf(subs={self.x[0]: t_})
                    else:
                        t1 = t_
                        f_val_t1 = self.f.evalf(subs={self.x[0]: t_})