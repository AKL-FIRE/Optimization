import optpy.Optimization as op
import sympy as sy
import random

class GoldSegment(op.Optimization):
    def __init__(self,useGUI,str_fun=None,epsilon=None,Search=None):
        super(GoldSegment, self).__init__(useGUI, str_fun, epsilon)
        if self.x.__len__() != 1:
            raise('非法的参数个数，只允许单变量函数。')
        if useGUI == False:
            t = self.GetX()
            self.a = t[0]
            self.b = t[1]
            print('该算法初始化完成。')
        else:
            if Search != '':
                str_search = Search.split(',')
                str_search = [float(x) for x in str_search]
                self.a = min(str_search)
                self.b = max(str_search)
            else:
                t = self.GetX()
                self.a = t[0]
                self.b = t[1]
            print('该算法初始化完成。')

    def Calculate(self):
        lambda_ = self.a + 0.382 * (self.b - self.a)
        miu_ = self.a + 0.618 * (self.b - self.a)
        k = 1
        f_value = 0
        while self.b - self.a >= self.epsilon:
            if self.f.subs({self.x[0]: lambda_}) > self.f.subs({self.x[0]: miu_}):
                self.a = lambda_
                self.b = self.b
                lambda_ = miu_
                miu_ = self.a + 0.618 * (self.b - self.a)
                f_value = self.f.subs({self.x[0]: miu_})
            else:
                self.a = self.a
                self.b = miu_
                miu_ = lambda_
                lambda_ = self.a + 0.382 * (self.b - self.a)
                f_value = self.f.subs({self.x[0]: lambda_})
            k = k + 1
        print('经过', k, '次迭代后得到的', '最优解的点为： ', self.x, ' = ', (self.a + self.b) / 2, ' 此点处函数值为：', f_value)
        output_str = '经过' + str(k) + '次迭代后得到的最优解的点为： ' + str(self.x) + '=' + str((self.a + self.b) / 2) + ' 此点处函数值为：' + str(
            f_value)
        return [self.a,self.b], f_value, output_str

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