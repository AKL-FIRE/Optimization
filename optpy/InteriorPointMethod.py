import optpy.Optimization as op
import sympy as sy

class InteriorPointMethod(op.Optimization):
    def __init__(self,useGUI,str_fun=None,epsilon=None):
        super(InteriorPointMethod,self).__init__(useGUI, str_fun, epsilon)

        self.beta = 0.1
        self.r = 10.0  # 初始惩罚因子
        str_constrain = input('请输入约束条件，以；分隔：')
        self.str_constrain = str_constrain.split(';')
        str_penalty = self.GeneratePenaltyFun(self.r, self.str_constrain)
        self.penalty_f = sy.simplify(str_penalty)
        self.f_str1 = self.f_str + '+' + str_penalty
        self.f = sy.simplify(self.f_str1)
        print(self.f_str1)

    def Calculate(self):
        k = 1
        from optpy import NewtonMethod
        while True:
            a = NewtonMethod.NewtonMethod(True,self.f_str1,self.epsilon)
            a.x_val = self.x_val
            result = a.Calculate()
            self.x_val = result[0]
            penalty_f = self.penalty_f
            for i in range(self.x_length):
                penalty_f = penalty_f.subs({self.x[i]:result[0][i]})
            if penalty_f <= self.epsilon:
                print(result[2])
                break
            else:
                self.r = self.r * self.beta
                k = k + 1
                str_penalty = self.GeneratePenaltyFun(self.r, self.str_constrain)
                self.penalty_f = sy.simplify(str_penalty)
                self.f_str1 = self.f_str + '+' + str_penalty
                self.f = sy.simplify(self.f_str1)


    def GeneratePenaltyFun(self,str_penalty_num,str_constrain):
        str_penalty = str(str_penalty_num) + '*('
        for i in str_constrain:
            str_penalty = str_penalty + '1/' + '(' + i + ')' + '+'
        str_penalty = str_penalty[0:len(str_penalty) - 1] + ')'
        return str_penalty

a = InteriorPointMethod(False)
a.Calculate()