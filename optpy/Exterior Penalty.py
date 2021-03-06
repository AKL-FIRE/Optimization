import sympy as sy
import optpy.Optimization as op

class ExteriorPenalty(op.Optimization):
    def __init__(self,useGUI,str_fun=None,epsilon=None):
        super(ExteriorPenalty, self).__init__(useGUI, str_fun, epsilon)
        self.theta = 1
        self.c = 10
        str_constrain_eaqual = input('请输入等式约束条件，以；分隔：')
        str_constrain_uneaqual = input('请输入不等式约束条件，以；分隔：')
        self.str_constrain_uneaqual = str_constrain_uneaqual.split(';')
        self.str_constrain_eaqual = str_constrain_eaqual.split(';')
        str_penalty = self.GeneratePenaltyFun(self.theta, self.str_constrain_eaqual,self.str_constrain_uneaqual)
        self.penalty_f = sy.simplify(str_penalty)
        self.f_str1 = self.f_str + '+' + str_penalty
        self.f = sy.simplify(self.f_str1)
        print(self.f_str1)

    def GeneratePenaltyFun(self,str_penalty_num,str_constrain_eaqual,str_constrain_uneaqual):
        str_penalty = str(str_penalty_num) + '*('
        for i in str_constrain_uneaqual:
            fun_ = sy.simplify(i)
            for index in range(self.x_length):
                fun_ = fun_.subs({self.x[index]:self.x_val[index]})
            if -1*fun_ > 0:
                str_penalty = str_penalty + '(' + i + ')**2+'
        for i in str_constrain_eaqual:
            str_penalty = str_penalty + '(' + i + ')**2+'
        str_penalty = str_penalty[0:len(str_penalty) - 1] + ')'
        return str_penalty

    def Calculate(self):
        k = 1
        from optpy import NewtonMethod
        while True:
            a = NewtonMethod.NewtonMethod(True, self.f_str1, self.epsilon)
            a.x_val = self.x_val
            result = a.Calculate()
            self.x_val = result[0]
            penalty_f = self.penalty_f
            for i in range(self.x_length):
                penalty_f = penalty_f.subs({self.x[i]: result[0][i]})
            if penalty_f <= self.epsilon:
                print(result[2])
                break
            else:
                self.theta = self.theta * self.c
                k = k + 1
                str_penalty = self.GeneratePenaltyFun(self.theta, self.str_constrain_eaqual,self.str_constrain_uneaqual)
                self.penalty_f = sy.simplify(str_penalty)
                self.f_str1 = self.f_str + '+' + str_penalty
                self.f = sy.simplify(self.f_str1)

a = ExteriorPenalty(False)
a.Calculate()